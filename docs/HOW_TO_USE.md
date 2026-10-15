# How to use this agent (plain language)

You do **not** need to know Python or Git to use this.

Think of this repo as a **recipe book for an AI assistant**.  
You open the recipe, tell the AI your situation, and it drafts answers.

---

## Before you start

Have ready (as much as you can):

1. **What** you are giving feedback about (person, product, service, etc.)
2. **How you feel** (positive, negative, moderate, extremely happy, extremely sad)
3. **What happened** in your own words (bullet points are fine)
4. **The questions** — typed out, screenshots, or a public survey link

Important:

- The agent drafts answers for **you** to review.
- It should **never** click Submit on a live form for you.
- Do not share passwords or private login codes with the AI.

---

## Option A — Cursor (easiest for many people)

1. Install [Cursor](https://cursor.com) if you do not have it.
2. In Cursor: **File → Open Folder** → choose this `feedback-answering-agent` folder.
3. Open **Chat** (Agent / Composer).
4. Paste:

```text
Read START_HERE.md, AGENTS.md, and prompts/feedback-agent.md.
Help me draft feedback. Do not submit any form.

Subject: ...
Sentiment: ...
What happened:
- ...
Questions:
1. ...
```

5. Read the draft. Edit anything that does not sound like you.
6. Paste the final text into the real survey yourself.

Tip: you can also say “use `templates/my-feedback-request.md` — I filled it in.”

---

## Option B — Claude Code

1. Open a terminal in this folder.
2. Start Claude Code in the project.
3. Paste the same starter message as in Option A.
4. Review the draft, then submit the form yourself.

---

## Option C — Claude.ai (web chat)

1. Start a new chat on Claude.
2. Attach (upload) these files:
   - `prompts/feedback-agent.md`
   - `templates/my-feedback-request.md` (after you fill it in)  
   or just paste your notes into the chat.
3. Say:

```text
Follow the Feedback Answering Agent instructions in the attached file.
Draft answers to my questions. Do not submit anything.
```

4. Review and copy the answers into your survey.

---

## Option D — ChatGPT / other chat AIs

Same as Claude.ai:

1. Upload `prompts/feedback-agent.md` (and your filled template if you have one).
2. Paste your questions and experience.
3. Ask for a **draft only**, then review before submitting.

---

## Option E — Antigravity or other agentic IDEs

1. Open this repository as the project folder.
2. Point the agent at `AGENTS.md` and `prompts/feedback-agent.md`.
3. Use the starter message from [START_HERE.md](../START_HERE.md).
4. Review drafts before submitting anything.

---

## Option F — Optional helper for technical users

If you are comfortable with a terminal, this command builds one big prompt you can paste into any AI:

```bash
python feedback_agent.py --input examples/product-feedback.json
```

Copy the printed text into Claude, ChatGPT, Cursor, etc.

You do **not** need this step to use the agent. Options A–E are enough.

---

## Simple flow diagram

```text
You describe what happened
        ↓
AI reads this repo's agent instructions
        ↓
AI drafts answers matching your sentiment
        ↓
You review and edit
        ↓
You submit the real form yourself
```

---

## If something goes wrong

| Problem | What to do |
|---|---|
| Survey link needs login | Paste the questions or send screenshots instead |
| Draft invents details | Say: “Only use facts I provided. Remove anything I did not say.” |
| Tone is wrong | Change the sentiment word and ask to rewrite |
| Too long / too short | Say: “Make answers short” or “Make answers detailed” |
| Multiple choice / star ratings | Ask: “Suggest which option fits, and explain why briefly” — you still pick the final choice |

---

## Privacy reminder

- Prefer general descriptions over private data (IDs, medical details, salaries).
- Do not commit filled templates with confidential notes to GitHub.
- Always read the draft before sending it anywhere.
