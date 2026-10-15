# Everyday use cases

Real-world situations this agent is meant for. Copy the example prompt and swap in your details.

---

## 1. Product or app survey

**When:** A company asks “How was the product?” after you used an app or website.

**Example prompt:**

```text
Read AGENTS.md and prompts/feedback-agent.md.
Draft product feedback. Do not submit anything.

Subject: TaskFlow mobile app
Type: product
Sentiment: moderate
Context: I use it for a small team of 4.
What happened:
- Board view makes ownership clear
- Notifications on phone often arrive late
- I want more control over notification settings
Questions:
1. What do you like most?
2. What could we improve?
3. Anything else?
Length: medium
```

---

## 2. Bad service experience

**When:** A late appointment, poor support call, or delivery problem.

**Example prompt:**

```text
Read AGENTS.md and prompts/feedback-agent.md.
Draft service feedback. Do not submit anything.

Subject: City Clinic appointment
Type: service
Sentiment: negative
What happened:
- Waited 45 minutes past my scheduled time
- Staff explained there was a delay
- Nobody gave an updated wait estimate
Questions:
1. What went well?
2. What should we improve?
3. Would you recommend us? (Yes / No / Maybe)
Length: short
```

---

## 3. Extremely happy customer

**When:** Something exceeded expectations and you want to say thank you clearly.

**Example prompt:**

```text
Read AGENTS.md and prompts/feedback-agent.md.
Draft feedback. Do not submit anything.

Subject: Acme Headphones
Type: product
Sentiment: extremely_happy
What happened:
- Battery lasted through a full work week of commuting
- Customer support replaced a broken cable in 2 days
- Comfortable for long calls
Questions: (paste from email survey)
Length: medium
```

---

## 4. Peer or person feedback

**When:** A workplace review asks about a colleague’s work (not personal life).

**Example prompt:**

```text
Read AGENTS.md and prompts/feedback-agent.md.
Draft person feedback. Do not submit anything.

Subject: Jordan Lee (project teammate)
Type: person
Sentiment: positive
Context: We worked together on Project Atlas for 3 months.
What I observed:
- Ran weekly standups that kept blockers visible
- Documented decisions in the shared wiki
- Helped two new joiners ramp up on the codebase
Questions:
1. What are their strengths?
2. What could they improve?
3. Would you work with them again?
```

Note: Stick to **work you saw**. Do not invent achievements or private details.

---

## 5. Survey link only

**When:** You have a public link but do not want to copy every question by hand.

**Example prompt:**

```text
Read AGENTS.md and prompts/feedback-agent.md.
Open this survey if you can browse. If not, ask me for screenshots.
Draft answers. Do not submit the form.

Survey URL: https://example.com/survey
Subject: Hotel weekend stay
Type: experience
Sentiment: extremely_sad
What happened:
- Room was not ready 2 hours after check-in time
- AC did not work overnight
- Front desk apologized but offered no compensation
```

If the AI cannot open the link, paste questions or screenshots.

---

## 6. Mixed / balanced review

**When:** Some things were good, some were not. You want fairness, not anger or fluff.

Use sentiment: **moderate**, and list both kinds of facts.

---

## What good looks like

- Answers match **your** facts
- Tone matches the sentiment you chose
- Each question gets its own answer (not copy-paste of the same paragraph)
- Ratings/choices are marked as **suggestions** until you confirm
- Nothing is submitted automatically
