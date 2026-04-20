import os
import json
from pathlib import Path
from typing import AsyncGenerator

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent / ".env")

WIKI_DIR = Path(__file__).parent.parent / "wiki"
PROVIDER = os.getenv("LLM_PROVIDER", "ollama").lower()
MAX_ARTICLE_CHARS = int(os.getenv("MAX_ARTICLE_CHARS", "800"))
MAX_CONTEXT_ARTICLES = int(os.getenv("MAX_CONTEXT_ARTICLES", "1"))

app = FastAPI()


def load_wiki_articles() -> dict[str, str]:
    articles = {}
    for md_file in WIKI_DIR.rglob("*.md"):
        if md_file.name in ("index.md", "log.md"):
            continue
        rel = str(md_file.relative_to(WIKI_DIR))
        articles[rel] = md_file.read_text(encoding="utf-8")
    return articles


def find_relevant(query: str, articles: dict[str, str]) -> list[tuple[str, str]]:
    tokens = set(query.lower().split())
    scores = {p: sum(1 for t in tokens if t in c.lower()) for p, c in articles.items()}
    ranked = sorted(scores, key=lambda p: scores[p], reverse=True)
    return [(p, articles[p][:MAX_ARTICLE_CHARS]) for p in ranked[:MAX_CONTEXT_ARTICLES] if scores[p] > 0]


class ChatRequest(BaseModel):
    messages: list[dict]
    query: str


async def safe_stream(gen: AsyncGenerator[str, None]) -> AsyncGenerator[str, None]:
    try:
        async for chunk in gen:
            yield chunk
    except Exception as e:
        yield f"data: {json.dumps({'content': f'\\n\\n⚠️ 錯誤：{e}'})}\n\n"
        yield "data: [DONE]\n\n"


async def stream_openai(
    base_url: str | None, api_key: str, model: str, system: str, messages: list[dict]
) -> AsyncGenerator[str, None]:
    from openai import AsyncOpenAI
    client = AsyncOpenAI(base_url=base_url, api_key=api_key)
    full_messages = [{"role": "system", "content": system}] + messages
    stream = await client.chat.completions.create(
        model=model, messages=full_messages, stream=True
    )
    async for chunk in stream:
        if not chunk.choices:
            continue
        delta = chunk.choices[0].delta.content
        if delta:
            yield f"data: {json.dumps({'content': delta})}\n\n"
    yield "data: [DONE]\n\n"


async def stream_anthropic(
    api_key: str, model: str, system: str, messages: list[dict]
) -> AsyncGenerator[str, None]:
    import anthropic
    client = anthropic.AsyncAnthropic(api_key=api_key)
    async with client.messages.stream(
        model=model, max_tokens=4096, system=system, messages=messages
    ) as stream:
        async for text in stream.text_stream:
            yield f"data: {json.dumps({'content': text})}\n\n"
    yield "data: [DONE]\n\n"


def build_system(relevant: list[tuple[str, str]]) -> str:
    if not relevant:
        return "你是 Kenny-Wiki 的知識庫助理。請使用繁體中文回答問題。"
    context = "\n\n---\n\n".join(content for _, content in relevant)
    return f"你是 Kenny-Wiki 的知識庫助理。根據以下內容回答，請用繁體中文簡潔回覆。\n\n{context}"


@app.get("/api/articles")
def list_articles():
    result = []
    for md_file in sorted(WIKI_DIR.rglob("*.md")):
        if md_file.name in ("index.md", "log.md"):
            continue
        rel = str(md_file.relative_to(WIKI_DIR))
        parts = Path(rel).parts
        category = parts[0] if len(parts) > 1 else "其他"
        title = Path(rel).stem.replace("-", " ")
        result.append({"path": rel, "title": title, "category": category})
    return result


@app.get("/api/article")
def get_article(path: str):
    target = (WIKI_DIR / path).resolve()
    if not target.is_relative_to(WIKI_DIR) or not target.exists():
        return {"content": ""}
    return {"content": target.read_text(encoding="utf-8")}


@app.get("/api/provider")
def get_provider():
    model_map = {
        "ollama": os.getenv("OLLAMA_MODEL", "llama3.2"),
        "openai": os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        "gemini": os.getenv("GEMINI_MODEL", "gemini-2.0-flash"),
        "anthropic": os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-6"),
        "nvidia": os.getenv("NVIDIA_MODEL", "minimaxai/minimax-m2.7"),
    }
    return {"provider": PROVIDER, "model": model_map.get(PROVIDER, "unknown")}


async def prepend_sources(source_paths: list[str], gen: AsyncGenerator[str, None]) -> AsyncGenerator[str, None]:
    if source_paths:
        yield f"data: {json.dumps({'sources': source_paths})}\n\n"
    async for chunk in gen:
        yield chunk


@app.post("/api/chat")
async def chat(req: ChatRequest):
    articles = load_wiki_articles()
    relevant = find_relevant(req.query, articles)
    source_paths = [p for p, _ in relevant]
    system = build_system(relevant)

    if PROVIDER == "ollama":
        gen = stream_openai(
            base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1"),
            api_key="ollama",
            model=os.getenv("OLLAMA_MODEL", "llama3.2"),
            system=system, messages=req.messages,
        )
    elif PROVIDER == "openai":
        gen = stream_openai(
            base_url=None,
            api_key=os.getenv("OPENAI_API_KEY", ""),
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            system=system, messages=req.messages,
        )
    elif PROVIDER == "gemini":
        gen = stream_openai(
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
            api_key=os.getenv("GEMINI_API_KEY", ""),
            model=os.getenv("GEMINI_MODEL", "gemini-2.0-flash"),
            system=system, messages=req.messages,
        )
    elif PROVIDER == "anthropic":
        gen = stream_anthropic(
            api_key=os.getenv("ANTHROPIC_API_KEY", ""),
            model=os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-6"),
            system=system, messages=req.messages,
        )
    elif PROVIDER == "nvidia":
        gen = stream_openai(
            base_url="https://integrate.api.nvidia.com/v1",
            api_key=os.getenv("NVIDIA_API_KEY", ""),
            model=os.getenv("NVIDIA_MODEL", "minimaxai/minimax-m2.7"),
            system=system, messages=req.messages,
        )
    else:
        async def err():
            yield f"data: {json.dumps({'content': f'未知的 LLM Provider: {PROVIDER}'})}\n\n"
            yield "data: [DONE]\n\n"
        gen = err()

    return StreamingResponse(prepend_sources(source_paths, safe_stream(gen)), media_type="text/event-stream")


app.mount(
    "/",
    StaticFiles(directory=Path(__file__).parent / "static", html=True),
    name="static",
)
