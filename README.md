# Universal Feedback Answering Agent

Draft evidence-based feedback for people, products, services,
experiences, and surveys.

Works through shared instructions with Cursor, Claude, Claude Code,
Antigravity, and other AI assistants that accept Markdown context.

## Features

- Five sentiment presets
- Free-text and choice/rating question support
- Optional survey links and public reference sources
- Firsthand-evidence safeguards
- Human review before submission
- Dependency-free prompt-building CLI

## Sentiments

| Value | Style |
|---|---|
| positive | Appreciative and constructive |
| negative | Critical, specific, and respectful |
| moderate | Balanced and measured |
| extremely_happy | Enthusiastic and grateful |
| extremely_sad | Disappointed or saddened, without hostility |

Sentiment never overrides facts.

## Quick start

Requires Python 3.10+.

```bash
git clone https://github.com/shahmeetk/feedback-answering-agent.git
cd feedback-answering-agent

python -m unittest discover -s tests -v
python feedback_agent.py --input examples/product-feedback.json
```

The CLI prints a complete prompt. Paste it into your chosen assistant.

It does not call an LLM, browse websites, or submit surveys.

## Use in Cursor, Claude Code, or Antigravity

Open the repository in your assistant and ask:

> Read AGENTS.md and prompts/feedback-agent.md.
> Use examples/product-feedback.json as the request.
> Draft answers to each question. Do not submit anything.

Do not rely on automatic instruction discovery: explicitly reference
the files when starting a session.

## Use in Claude or another chat assistant

1. Generate the prompt using the CLI.
2. Paste its output into the chat.
3. Provide screenshots or question text if links are inaccessible.
4. Review the resulting answers.

Alternatively, attach prompts/feedback-agent.md and your request JSON.

## Create a request

Copy examples/product-feedback.json and replace its values.

Required:
- subject_type
- subject_name
- sentiment
- questions or survey_url

Optional:
- context
- observations
- reference_urls
- language
- length: short, medium, detailed

Questions are strings. Include full options and scale labels in the
question text for rating or multiple-choice questions.

A URL-only request requires an assistant with browsing access.
Otherwise, supply the questions directly.

## Example interactive request

> Help me complete a service survey.
> Sentiment: negative.
> I waited 45 minutes beyond the scheduled appointment.
> Staff explained the delay but did not provide an updated estimate.
> Questions: What went well? What should improve?
> Keep answers short and constructive.

## Privacy and integrity

- Do not commit confidential feedback or personal data.
- Review your AI provider's data-handling settings before sharing.
- Public profile information is background, not proof of performance.
- Never fabricate experiences or testimonials.
- Review all ratings and answers yourself.
- This agent does not submit forms.

## Tests

```bash
python -m unittest discover -s tests -v
```

## Contributing through a pull request

If you have write access:

```bash
git switch -c feat/universal-feedback-agent
git add AGENTS.md CLAUDE.md README.md feedback_agent.py prompts examples tests
git commit -m "Add portable universal feedback drafting agent"
git push -u origin feat/universal-feedback-agent
```

Then open a pull request on GitHub.

Without write access, fork the repository first and open a pull request
from your fork.

If GitHub CLI is installed and authenticated:

```bash
gh pr create \
  --title "Add universal feedback drafting agent" \
  --body "Adds portable instructions, sentiment presets, CLI, examples, and tests."
```

## Limitations

- Browser access depends on the assistant being used.
- Authenticated survey pages may require copied text or screenshots.
- Model output requires human verification.
- The included tests validate prompt construction, not model behavior.
