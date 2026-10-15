# Claude / Claude Code — project context

This repo is a **portable Feedback Answering Agent**.

Before drafting feedback:

1. Read `AGENTS.md`
2. Read `prompts/feedback-agent.md`
3. If the user filled it in, use `templates/my-feedback-request.md`

Point non-technical users to `START_HERE.md` and `docs/HOW_TO_USE.md`.

## Behavior

- Draft only — do not submit surveys
- Stay evidence-based; do not invent experiences
- Support all five sentiments and all subject types
- Do not assume browsing is available; if a link fails, ask for pasted questions or screenshots

## Checks (optional)

```bash
python -m unittest discover -s tests -v
```
