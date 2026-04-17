const messagesEl = document.getElementById('messages');
const inputEl = document.getElementById('input');
const sendBtn = document.getElementById('send-btn');
const clearBtn = document.getElementById('clear-btn');
const articleListEl = document.getElementById('article-list');
const providerBadge = document.getElementById('provider-badge');
const modal = document.getElementById('modal');
const modalBackdrop = document.getElementById('modal-backdrop');
const modalClose = document.getElementById('modal-close');
const modalTitle = document.getElementById('modal-title');
const modalBody = document.getElementById('modal-body');

let chatHistory = [];
let isStreaming = false;

// ── Provider badge ──────────────────────────────────────────
async function loadProvider() {
  try {
    const res = await fetch('/api/provider');
    const { provider, model } = await res.json();
    providerBadge.textContent = `${provider} · ${model}`;
  } catch {
    providerBadge.textContent = '連線失敗';
  }
}

// ── Article list ─────────────────────────────────────────────
async function loadArticles() {
  try {
    const res = await fetch('/api/articles');
    const articles = await res.json();

    const grouped = {};
    for (const a of articles) {
      (grouped[a.category] ??= []).push(a);
    }

    articleListEl.innerHTML = '';
    for (const [cat, items] of Object.entries(grouped)) {
      const label = document.createElement('div');
      label.className = 'category-label';
      label.textContent = cat;
      articleListEl.appendChild(label);

      for (const item of items) {
        const btn = document.createElement('button');
        btn.className = 'article-item';
        btn.textContent = item.title;
        btn.onclick = () => openArticle(item.path, item.title);
        articleListEl.appendChild(btn);
      }
    }
  } catch {
    articleListEl.innerHTML = '<div style="color:#475569;padding:10px;font-size:12px;">無法載入文章列表</div>';
  }
}

// ── Article modal ─────────────────────────────────────────────
async function openArticle(path, title) {
  modalTitle.textContent = title;
  modalBody.innerHTML = '<div style="color:#94a3b8;padding:20px 0">載入中…</div>';
  modal.classList.remove('hidden');

  const res = await fetch(`/api/article?path=${encodeURIComponent(path)}`);
  const { content } = await res.json();
  modalBody.innerHTML = marked.parse(content || '（無內容）');
}

modalClose.onclick = () => modal.classList.add('hidden');
modalBackdrop.onclick = () => modal.classList.add('hidden');
document.addEventListener('keydown', e => { if (e.key === 'Escape') modal.classList.add('hidden'); });

// ── Chat ──────────────────────────────────────────────────────
function appendMessage(role, html, isRaw = false) {
  const div = document.createElement('div');
  div.className = `message ${role}`;
  const bubble = document.createElement('div');
  bubble.className = 'bubble';
  if (isRaw) bubble.innerHTML = html;
  else bubble.textContent = html;
  div.appendChild(bubble);
  messagesEl.appendChild(div);
  messagesEl.scrollTop = messagesEl.scrollHeight;
  return bubble;
}

async function sendMessage() {
  const text = inputEl.value.trim();
  if (!text || isStreaming) return;

  isStreaming = true;
  sendBtn.disabled = true;
  inputEl.value = '';
  inputEl.style.height = 'auto';

  appendMessage('user', text);
  chatHistory.push({ role: 'user', content: text });

  const aiBubble = appendMessage('ai', '', true);
  aiBubble.classList.add('cursor');
  aiBubble.innerHTML = '';

  let fullText = '';

  try {
    const res = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ messages: chatHistory, query: text }),
    });

    const reader = res.body.getReader();
    const decoder = new TextDecoder();
    let buffer = '';

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;

      buffer += decoder.decode(value, { stream: true });
      const lines = buffer.split('\n');
      buffer = lines.pop();

      for (const line of lines) {
        if (!line.startsWith('data: ')) continue;
        const data = line.slice(6);
        if (data === '[DONE]') break;
        try {
          const { content } = JSON.parse(data);
          fullText += content;
          aiBubble.innerHTML = marked.parse(fullText);
          messagesEl.scrollTop = messagesEl.scrollHeight;
        } catch { /* ignore parse errors */ }
      }
    }
  } catch (err) {
    aiBubble.innerHTML = `<span style="color:#ef4444">連線錯誤：${err.message}</span>`;
  }

  aiBubble.classList.remove('cursor');
  chatHistory.push({ role: 'assistant', content: fullText });

  isStreaming = false;
  sendBtn.disabled = false;
  inputEl.focus();
}

// ── Input behaviour ───────────────────────────────────────────
inputEl.addEventListener('keydown', e => {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault();
    sendMessage();
  }
});

inputEl.addEventListener('input', () => {
  inputEl.style.height = 'auto';
  inputEl.style.height = Math.min(inputEl.scrollHeight, 160) + 'px';
});

sendBtn.onclick = sendMessage;

clearBtn.onclick = () => {
  chatHistory = [];
  messagesEl.innerHTML = '';
  appendMessage('ai',
    '對話已清除。請輸入新的問題，我會根據知識庫內容回答你。',
    false
  );
};

// ── Init ──────────────────────────────────────────────────────
loadProvider();
loadArticles();
