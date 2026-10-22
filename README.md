<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content="Ankith — builder of AI tools, web experiences, and smart productivity systems." />
    <title>Ankith | AI Builder & Product Engineer</title>
    <style>
      :root {
        --bg: #06121f;
        --bg-alt: #0f172a;
        --panel: rgba(15, 23, 42, 0.82);
        --panel-strong: #101827;
        --card: rgba(15, 23, 42, 0.75);
        --primary: #7c3aed;
        --primary-2: #8b5cf6;
        --accent: #22c55e;
        --text: #edf2ff;
        --muted: #b8c2d8;
        --line: rgba(148, 163, 184, 0.18);
        --glow: rgba(124, 58, 237, 0.34);
      }

      * { box-sizing: border-box; }
      html { scroll-behavior: smooth; }
      body {
        margin: 0;
        font-family: Inter, "Segoe UI", Arial, sans-serif;
        background: radial-gradient(circle at top, rgba(124,58,237,0.2), transparent 30%),
                    linear-gradient(135deg, #020817 0%, #0f172a 35%, #111827 100%);
        color: var(--text);
        line-height: 1.6;
      }

      a { color: inherit; text-decoration: none; }
      img { max-width: 100%; display: block; }
      .container {
        width: min(1180px, calc(100% - 32px));
        margin: 0 auto;
      }

      .topbar {
        position: sticky;
        top: 0;
        z-index: 50;
        backdrop-filter: blur(18px);
        background: rgba(6, 18, 31, 0.7);
        border-bottom: 1px solid var(--line);
      }

      .nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        min-height: 72px;
      }

      .brand {
        font-size: 1.35rem;
        font-weight: 800;
        letter-spacing: 0.05em;
      }

      .brand span {
        color: #a78bfa;
      }

      .nav-links {
        display: flex;
        gap: 22px;
        color: var(--muted);
        font-size: 0.95rem;
      }

      .nav-links a:hover { color: var(--text); }
      .nav-cta {
        background: linear-gradient(135deg, var(--primary), var(--primary-2));
        border: 1px solid rgba(167, 139, 250, 0.5);
        border-radius: 999px;
        padding: 10px 16px;
        color: white;
        font-weight: 700;
      }

      .hero {
        padding: 84px 0 52px;
      }

      .hero-inner {
        display: grid;
        grid-template-columns: 1.1fr 0.9fr;
        gap: 28px;
        align-items: center;
      }

      .eyebrow {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        border: 1px solid rgba(124, 58, 237, 0.5);
        background: rgba(124, 58, 237, 0.08);
        color: #ddd6fe;
        border-radius: 999px;
        padding: 8px 14px;
        font-size: 0.8rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
      }

      h1 {
        margin: 20px 0 14px;
        font-size: clamp(2.7rem, 5vw, 5rem);
        line-height: 1.02;
        letter-spacing: -0.06em;
      }

      .gradient-text {
        background: linear-gradient(135deg, #e9d5ff 0%, #a78bfa 30%, #83d8ff 100%);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
      }

      .lead {
        color: var(--muted);
        font-size: 1.08rem;
        max-width: 640px;
      }

      .hero-actions {
        display: flex;
        flex-wrap: wrap;
        gap: 16px;
        margin-top: 26px;
      }

      .btn {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        border-radius: 14px;
        padding: 14px 20px;
        font-weight: 700;
        transition: transform 0.15s ease, filter 0.15s ease;
      }

      .btn:hover { transform: translateY(-1px); filter: brightness(1.05); }
      .btn-primary {
        background: linear-gradient(135deg, var(--primary), var(--primary-2));
        color: white;
      }
      .btn-secondary {
        background: rgba(15, 23, 42, 0.7);
        border: 1px solid var(--line);
        color: var(--text);
      }

      .hero-stats {
        display: flex;
        gap: 26px;
        flex-wrap: wrap;
        margin-top: 28px;
      }

      .stat strong {
        display: block;
        font-size: 1.65rem;
        margin-bottom: 4px;
      }
      .stat span {
        color: var(--muted);
      }

      .profile-card {
        position: relative;
        background: linear-gradient(180deg, rgba(17, 24, 39, 0.95), rgba(15, 23, 42, 0.72));
        border: 1px solid var(--line);
        border-radius: 24px;
        padding: 18px;
        box-shadow: 0 30px 80px rgba(124, 58, 237, 0.24);
      }

      .profile-box {
        background: linear-gradient(180deg, rgba(124,58,237,0.12), rgba(15,23,42,0.3));
        border-radius: 20px;
        padding: 22px;
        border: 1px solid rgba(163, 176, 220, 0.18);
      }

      .avatar {
        width: 86px;
        height: 86px;
        border-radius: 24px;
        display: grid;
        place-items: center;
        font-size: 2rem;
        font-weight: 800;
        background: linear-gradient(135deg, #8b5cf6, #22d3ee);
        color: white;
        box-shadow: 0 18px 40px rgba(124, 58, 237, 0.48);
      }

      .tag-row {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-top: 18px;
      }
      .tag {
        background: rgba(148, 163, 184, 0.08);
        border: 1px solid rgba(148, 163, 184, 0.16);
        color: var(--muted);
        border-radius: 999px;
        padding: 7px 11px;
        font-size: 0.76rem;
      }

      .mini-card {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: rgba(11, 17, 29, 0.9);
        border: 1px solid var(--line);
        border-radius: 14px;
        padding: 12px 14px;
        margin-top: 16px;
        color: var(--muted);
      }

      .section {
        padding: 30px 0 20px;
      }

      .section-header {
        display: flex;
        justify-content: space-between;
        align-items: end;
        gap: 18px;
        margin-bottom: 18px;
      }

      .section-label {
        color: #c4b5fd;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        font-size: 0.76rem;
        font-weight: 700;
      }

      .section-header h2 {
        margin: 8px 0 0;
        font-size: clamp(1.9rem, 3vw, 3rem);
        letter-spacing: -0.06em;
      }

      .cards {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 20px;
      }

      .card {
        background: var(--card);
        border: 1px solid var(--line);
        border-radius: 20px;
        padding: 22px;
      }

      .card h3 {
        margin: 0 0 12px;
        font-size: 1.3rem;
      }
      .card p {
        margin: 0;
        color: var(--muted);
      }

      .feature-list {
        list-style: none;
        padding: 0;
        margin: 18px 0 0;
        display: grid;
        gap: 10px;
      }
      .feature-list li {
        color: var(--muted);
        position: relative;
        padding-left: 18px;
      }
      .feature-list li::before {
        content: "•";
        position: absolute;
        left: 0;
        color: #a78bfa;
      }

      .showcase {
        display: grid;
        grid-template-columns: 1.15fr 0.85fr;
        gap: 22px;
        margin-top: 20px;
      }

      .panel {
        background: var(--panel);
        border: 1px solid var(--line);
        border-radius: 22px;
        padding: 24px;
      }

      .project-list {
        display: grid;
        gap: 14px;
      }
      .project-item {
        display: flex;
        align-items: center;
        justify-content: space-between;
        border: 1px solid var(--line);
        border-radius: 16px;
        padding: 16px 18px;
        background: rgba(15, 23, 42, 0.7);
      }
      .project-name {
        font-weight: 700;
      }
      .project-meta {
        color: var(--muted);
        font-size: 0.9rem;
      }
      .project-tag {
        border-radius: 999px;
        background: rgba(34,197,94,0.1);
        border: 1px solid rgba(34,197,94,0.45);
        color: #bbf7d0;
        padding: 8px 12px;
        font-size: 0.75rem;
      }

      .assistant-box {
        background: linear-gradient(180deg, rgba(124,58,237,0.12), rgba(15,23,42,0.8));
        border: 1px solid rgba(168, 85, 247, 0.25);
        border-radius: 20px;
        overflow: hidden;
      }

      .assistant-head {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 18px 20px;
        border-bottom: 1px solid rgba(148,163,184,0.15);
      }
      .assistant-head strong { font-size: 1.05rem; }
      .online { color: #86efac; }

      .assistant-chat {
        padding: 18px 20px 14px;
        min-height: 190px;
        display: flex;
        flex-direction: column;
        gap: 12px;
      }
      .bubble {
        max-width: 82%;
        padding: 12px 14px;
        border-radius: 16px;
        font-size: 0.95rem;
        line-height: 1.5;
      }
      .bubble.ai {
        background: rgba(15, 23, 42, 0.85);
        border: 1px solid rgba(148,163,184,0.15);
        color: var(--text);
      }
      .bubble.user {
        background: linear-gradient(135deg, var(--primary), var(--primary-2));
        margin-left: auto;
      }

      .assistant-input {
        display: flex;
        gap: 10px;
        padding: 0 20px 20px;
      }
      .assistant-input input {
        flex: 1;
        background: rgba(15, 23, 42, 0.78);
        border: 1px solid rgba(148,163,184,0.2);
        color: var(--text);
        border-radius: 12px;
        padding: 12px 14px;
        font-size: 0.98rem;
      }
      .assistant-input button {
        border: 0;
        border-radius: 12px;
        padding: 12px 18px;
        background: linear-gradient(135deg, var(--primary), var(--primary-2));
        color: white;
        font-weight: 700;
        cursor: pointer;
      }

      .contact-wrap {
        display: grid;
        grid-template-columns: 1.1fr 0.9fr;
        gap: 22px;
        align-items: center;
      }

      .contact-links {
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
        margin-top: 18px;
      }
      .contact-links a {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        height: 44px;
        padding: 0 16px;
        border-radius: 12px;
        background: rgba(15, 23, 42, 0.8);
        border: 1px solid var(--line);
        color: var(--text);
      }

      footer {
        padding: 34px 0 70px;
        color: var(--muted);
        text-align: center;
      }

      @media (max-width: 920px) {
        .hero-inner,
        .showcase,
        .contact-wrap,
        .cards {
          grid-template-columns: 1fr;
        }
        .nav-links {
          display: none;
        }
      }
    </style>
  </head>
  <body>
    <header class="topbar">
      <div class="container nav">
        <div class="brand">Ankith<span>.</span></div>
        <nav class="nav-links">
          <a href="#about">About</a>
          <a href="#work">Work</a>
          <a href="#tools">Tools</a>
          <a href="#contact">Contact</a>
        </nav>
        <a class="nav-cta" href="#contact">Let’s build</a>
      </div>
    </header>

    <main>
      <section class="hero">
        <div class="container hero-inner">
          <div>
            <div class="eyebrow">AI builder • product thinker</div>
            <h1>I design <span class="gradient-text">smarter digital experiences</span>.</h1>
            <p class="lead">
              I build AI-powered products, productivity systems, and polished web experiences that help people move faster,
              think clearer, and ship better.
            </p>
            <div class="hero-actions">
              <a class="btn btn-primary" href="#work">See my work</a>
              <a class="btn btn-secondary" href="#contact">Book a chat</a>
            </div>
            <div class="hero-stats">
              <div class="stat"><strong>3+</strong><span>Years building</span></div>
              <div class="stat"><strong>20+</strong><span>Projects shipped</span></div>
              <div class="stat"><strong>100%</strong><span>Product-focused</span></div>
            </div>
          </div>

          <div class="profile-card">
            <div class="profile-box">
              <div class="avatar">A</div>
              <div style="margin-top: 18px;">
                <div style="font-size: 1.5rem; font-weight: 800;">Ankith</div>
                <div style="color: var(--muted);">AI Product Engineer</div>
              </div>
              <div class="tag-row">
                <span class="tag">Python</span>
                <span class="tag">FastAPI</span>
                <span class="tag">React</span>
                <span class="tag">AI Apps</span>
                <span class="tag">UX</span>
              </div>
              <div class="mini-card">
                <span>Currently building</span>
                <strong style="color: var(--text);">AI productivity platforms</strong>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section id="about" class="section">
        <div class="container">
          <div class="section-header">
            <div>
              <div class="section-label">About</div>
              <h2>Product-minded builder with a systems mindset.</h2>
            </div>
          </div>

          <div class="cards">
            <article class="card">
              <h3>Strategy</h3>
              <p>I turn rough ideas into focused roadmaps, clear user value, and elegant product direction.</p>
              <ul class="feature-list">
                <li>Product planning</li>
                <li>Feature prioritization</li>
                <li>Experience design</li>
              </ul>
            </article>

            <article class="card">
              <h3>Design</h3>
              <p>I craft interfaces that are usable, modern, and built around clear user outcomes.</p>
              <ul class="feature-list">
                <li>Landing pages</li>
                <li>Dashboards</li>
                <li>Interaction flows</li>
              </ul>
            </article>

            <article class="card">
              <h3>Build</h3>
              <p>I bring ideas to life through clean engineering, automation, and AI integrations.</p>
              <ul class="feature-list">
                <li>FastAPI apps</li>
                <li>AI workflows</li>
                <li>Scalable web products</li>
              </ul>
            </article>
          </div>
        </div>
      </section>

      <section id="work" class="section">
        <div class="container">
          <div class="section-header">
            <div>
              <div class="section-label">Selected work</div>
              <h2>Building tools that make work feel lighter.</h2>
            </div>
          </div>

          <div class="showcase">
            <div class="panel">
              <div class="project-list">
                <div class="project-item">
                  <div>
                    <div class="project-name">AI Productivity Assistant</div>
                    <div class="project-meta">Productivity assistant with smart planning and workflow help</div>
                  </div>
                  <span class="project-tag">Live demo</span>
                </div>

                <div class="project-item">
                  <div>
                    <div class="project-name">Workflow Automation Platform</div>
                    <div class="project-meta">Reducing repetitive tasks through software and logic</div>
                  </div>
                  <span class="project-tag">Product</span>
                </div>

                <div class="project-item">
                  <div>
                    <div class="project-name">Portfolio & Brand Experience</div>
                    <div class="project-meta">Modern web presence built for clarity and personal branding</div>
                  </div>
                  <span class="project-tag">Brand</span>
                </div>
              </div>
            </div>

            <div class="assistant-box">
              <div class="assistant-head">
                <strong>AI assistant</strong>
                <span class="online">● online</span>
              </div>
              <div class="assistant-chat" id="assistant-chat">
                <div class="bubble ai">Hi! I can help plan your week, summarize work, and turn rough ideas into action.</div>
              </div>
              <div class="assistant-input">
                <input id="assistant-input" type="text" placeholder="Ask for a plan, summary, or task list..." />
                <button id="assistant-send">Send</button>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section id="tools" class="section">
        <div class="container">
          <div class="section-header">
            <div>
              <div class="section-label">Tools</div>
              <h2>Stacked for product velocity.</h2>
            </div>
          </div>

          <div class="cards">
            <article class="card">
              <h3>Frontend</h3>
              <p>Modern, responsive experiences with a clean and conversion-focused feel.</p>
              <ul class="feature-list">
                <li>HTML / CSS / JavaScript</li>
                <li>Responsive design</li>
                <li>User experience polish</li>
              </ul>
            </article>

            <article class="card">
              <h3>Backend</h3>
              <p>Fast, maintainable systems for AI, APIs, automation, and internal tools.</p>
              <ul class="feature-list">
                <li>Python</li>
                <li>FastAPI</li>
                <li>API integrations</li>
              </ul>
            </article>

            <article class="card">
              <h3>AI & Ops</h3>
              <p>Smart workflows and AI-powered experiences that reduce friction and increase output.</p>
              <ul class="feature-list">
                <li>Prompt-driven design</li>
                <li>Automation tooling</li>
                <li>Product experimentation</li>
              </ul>
            </article>
          </div>
        </div>
      </section>

      <section id="contact" class="section">
        <div class="container contact-wrap">
          <div>
            <div class="section-label">Contact</div>
            <h2 style="margin: 10px 0 12px; font-size: clamp(2rem, 3vw, 3rem); letter-spacing: -0.06em;">Let’s build the next useful thing.</h2>
            <p style="color: var(--muted); max-width: 620px;">
              Whether you’re launching a product, improving a workflow, or designing a stronger digital presence,
              I’d love to help turn the idea into something real.
            </p>
            <div class="contact-links">
              <a href="mailto:hello@ankith.com">hello@ankith.com</a>
              <a href="https://github.com/hnankith2006-bit" target="_blank" rel="noreferrer">GitHub</a>
              <a href="https://www.linkedin.com" target="_blank" rel="noreferrer">LinkedIn</a>
            </div>
          </div>

          <div class="panel">
            <div style="font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.1em; color: #c4b5fd; margin-bottom: 8px;">Availability</div>
            <div style="font-size: 2rem; font-weight: 800;">Open for projects</div>
            <p style="color: var(--muted); margin-top: 12px;">
              Product design, AI app prototyping, web development, and smart workflow systems.
            </p>
            <a class="btn btn-primary" href="mailto:hello@ankith.com" style="margin-top: 12px;">Start a conversation</a>
          </div>
        </div>
      </section>
    </main>

    <footer>
      <div class="container">© 2026 Ankith — building useful digital products.</div>
    </footer>

    <script>
      const chat = document.getElementById('assistant-chat');
      const input = document.getElementById('assistant-input');
      const send = document.getElementById('assistant-send');

      const addBubble = (text, who) => {
        const el = document.createElement('div');
        el.className = `bubble ${who}`;
        el.textContent = text;
        chat.appendChild(el);
        chat.scrollTop = chat.scrollHeight;
      };

      const askAssistant = async () => {
        const text = input.value.trim();
        if (!text) return;

        addBubble(text, 'user');
        input.value = '';

        try {
          const response = await fetch('/api/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: text, tasks: ['Ship homepage', 'Improve landing copy', 'Plan product next steps'] })
          });

          if (!response.ok) throw new Error('Request failed');
          const data = await response.json();
          addBubble(data.reply, 'ai');
        } catch (error) {
          addBubble('I’m here to help. Try asking for a plan, summary, or project next steps.', 'ai');
        }
      };

      send.addEventListener('click', askAssistant);
      input.addEventListener('keydown', (event) => {
        if (event.key === 'Enter') askAssistant();
      });
    </script>
  </body>
</html>
