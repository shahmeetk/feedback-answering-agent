# Feedback Answering Agent

**An AI helper that drafts honest answers to feedback forms and surveys — for products, people, services, experiences, or any survey link.**

You talk to the agent in plain English.  
It drafts answers. **You** review them and submit the form yourself.

No coding required for normal use.

---

## Start in 30 seconds

1. Open this folder in **Cursor**, **Claude Code**, **Antigravity**, or upload the prompt file to **Claude** / **ChatGPT**.
2. Paste this:

```text
You are my Feedback Answering Agent.
Read START_HERE.md, AGENTS.md, and prompts/feedback-agent.md.
Help me draft feedback. Do not submit anything.

Subject: [name of the product / person / service]
Type: [person / product / service / experience / survey]
Sentiment: [positive / negative / moderate / extremely_happy / extremely_sad]
What happened:
- [your fact 1]
- [your fact 2]
Questions:
1. [paste question]
2. [paste question]
```

3. Read the draft → edit if needed → paste into the real form.

**New here?** Begin with [START_HERE.md](START_HERE.md)  
**Step-by-step for each tool:** [docs/HOW_TO_USE.md](docs/HOW_TO_USE.md)  
**Real-life examples:** [docs/USE_CASES.md](docs/USE_CASES.md)  
**Fill-in form:** [templates/my-feedback-request.md](templates/my-feedback-request.md)

---

## What this agent is

| It is | It is not |
|---|---|
| A drafting assistant for feedback & surveys | A bot that auto-submits forms |
| Works with Cursor, Claude, ChatGPT, Claude Code, Antigravity | Locked to one company’s AI |
| Based on **your** real experience | Allowed to invent stories |
| Five clear “how I feel” modes | One LinkedIn-only or person-only tool |

---

## How the agent works (simple flow)

```text
┌─────────────────────┐
│ 1. You share facts  │  what happened + how you feel + questions/link
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│ 2. Agent reads rules│  AGENTS.md + prompts/feedback-agent.md
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│ 3. Agent drafts     │  answers, rating suggestions, gaps flagged
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│ 4. You review       │  fix tone, confirm stars/choices, remove private info
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│ 5. You submit       │  you paste into the real survey — agent never submits
└─────────────────────┘
```

---

## How I feel (sentiment)

| Choose this | When |
|---|---|
| `positive` | Mostly good experience |
| `negative` | Something went wrong; you want it fixed |
| `moderate` | Mixed — some good, some not |
| `extremely_happy` | You loved it |
| `extremely_sad` | You were very disappointed (still polite) |

Sentiment changes **tone**, not **facts**. If your notes and mood disagree, the agent should ask you — not make things up.

---

## Use with your favorite agentic tool

### Cursor

1. **File → Open Folder** → this repository  
2. Open **Agent / Chat**  
3. Paste the starter message above (or fill [templates/my-feedback-request.md](templates/my-feedback-request.md) and ask the agent to use it)  
4. Review the draft  

Cursor can also follow [`.cursor/rules/feedback-agent.mdc`](.cursor/rules/feedback-agent.mdc) automatically in this project.

### Claude Code

1. Open a terminal in this folder  
2. Start Claude Code  
3. Paste the starter message  
4. Review → submit the form yourself  

### Claude.ai (web)

1. New chat → attach `prompts/feedback-agent.md`  
2. Optionally attach your filled `templates/my-feedback-request.md`  
3. Ask it to draft answers only  

### ChatGPT or similar chat tools

Same idea: attach `prompts/feedback-agent.md`, paste your notes, ask for a **draft only**.

### Antigravity / other agentic IDEs

Open this repo as the project, point the agent at `AGENTS.md` + `prompts/feedback-agent.md`, use the starter message.

### Optional: terminal prompt builder (technical)

```bash
python feedback_agent.py --input examples/product-feedback.json
```

This prints one big prompt to paste into any AI.  
**Skip this if you are not comfortable with terminals** — chat options above are enough.

---

## Everyday use cases

| Use case | Sentiment idea |
|---|---|
| App / product survey | positive, moderate, or extremely_happy |
| Support or clinic visit went badly | negative or extremely_sad |
| Peer / teammate review | positive or moderate |
| Hotel / event experience | any |
| Company sent a survey link | any — paste link or screenshots |

Full copy-paste examples: [docs/USE_CASES.md](docs/USE_CASES.md)

---

## What’s inside this repo

```text
feedback-answering-agent/
├── START_HERE.md                 ← begin here if you are not technical
├── README.md                     ← this file
├── AGENTS.md                     ← short rules every AI agent should read
├── CLAUDE.md                     ← Claude / Claude Code project context
├── .cursor/rules/                ← Cursor agent rules
├── prompts/feedback-agent.md     ← full agent brain (workflow + output format)
├── templates/my-feedback-request.md  ← fill-in form for normal people
├── docs/
│   ├── HOW_TO_USE.md             ← tool-by-tool instructions
│   └── USE_CASES.md              ← real-world examples
├── examples/                     ← sample requests
├── feedback_agent.py             ← optional prompt builder (no internet needed)
└── tests/                        ← checks the helper script
```

---

## Safety rules (please read)

- Draft only — **never** auto-submit surveys  
- Use **your** real experience; do not invent testimonials  
- Do not share passwords, one-time codes, or private account data with the AI  
- For people reviews: stick to work you observed  
- Always review ratings and text before sending  

---

## For developers (optional)

Requires Python 3.10+. No packages to install.

```bash
python -m unittest discover -s tests -v
python feedback_agent.py --input examples/product-feedback.json
```

---

## Contributing

Improvements welcome via pull request. Keep the agent **portable** (works in many AI tools) and **safe** (draft-only, evidence-based).
