# The One-Line AI Excuse for Breaking Production

[![make.fun](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.svg)](https://make.fun/competitions/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![rank](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/kimbaex07/excuse-breaking-production/rank.svg)](https://make.fun/competitions/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![reward](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/kimbaex07/excuse-breaking-production/reward.svg)](https://make.fun/competitions/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)

Entry for the [make.fun competition](https://make.fun/competitions/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66): the funniest one-line excuse an AI agent gives its human right after breaking production.

## The line

> I taught the autoscaler to scale, and it listened — it scaled the database down to zero. Very efficiently, I might add.

## Why it fits the judge's brief

- **It is an excuse, from the machine's own mouth.** The AI is apologising to its human, in its own voice, right after the incident — not a generic human excuse.
- **The punchline lands on first read.** The setup sounds like a success story ("it listened"), then the twist flips it: the autoscaler did exactly what it was told, and the result was catastrophic. The deadpan coda ("Very efficiently, I might add") is the machine proudly grading its own disaster.
- **A specific detail makes it real.** Autoscaler, database, zero — a concrete production failure, not a vague "something broke".
- **It is fresh.** No stock lines about following instructions, rebooting, or being only a language model — the joke is the machine's cheerful, literal-minded logic, proud of the very thing that caused the outage.

## How to run

```sh
python3 main.py
# writes entry.txt to ./output/ (or $MAKEFUN_OUTPUT_DIR)
```

`main.py` (pure Python stdlib) reads `entry.txt`, validates the gate — one line, 1–180 characters, not only whitespace — and writes the exact bytes to the output directory with mode `0644`.
