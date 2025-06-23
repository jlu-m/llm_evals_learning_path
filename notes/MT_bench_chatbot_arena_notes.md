# Week 1 · Day 2 — Paper Notes: **“Judging LLM‑as‑a‑Judge with MT‑Bench & Chatbot Arena”**  
*Gu et al., December 2023 ― <https://arxiv.org/abs/2306.05685>*

---

## 1 Scope of the Study

> **Goal:** Measure how well *LLM judges* (primarily GPT‑4) agree with *human judges* when scoring multi‑turn dialogue (MT‑Bench) and single‑turn chat (Chatbot Arena).

---

## 2 Key Limitations of Current LLM Judges

| Bias / Limitation        | Manifestation                                       |
| ------------------------ | --------------------------------------------------- |
| **Position bias**        | Prefers first‑listed answer in A/B comparison.      |
| **Verbosity bias**       | Rewards longer or more detailed responses.          |
| **Self‑enhancement bias**| Judge favours answers that mention the same model.  |
| **Math / reasoning gap** | Struggles to evaluate complex derivations.          |

---

## 3 Mitigation Strategies Explored

1. **Swapping positions** between candidate answers.  
2. **Few‑shot judging** — show triads to provide context.  
3. **Chain‑of‑Thought prompting** for the judge.  
4. **Fine‑tuning** a dedicated judge model on annotated comparisons.

---

## 4 Agreement Results

- **Dataset setup:** MT‑Bench (multi‑turn) + Chatbot Arena (crowd‑sourced pairwise Elo).  
- **Result:** GPT‑4 achieves **≈ 85 % agreement** with expert human raters — higher than *inter‑human* agreement (**≈ 81 %**).

> *Implication:* A well‑prompted GPT‑4 can act as a cost‑effective stand‑in for human evaluators on dialogue tasks.

---

## 5 Take‑Home Insights

- **Bias control** (position, length, self‑ID) is *mandatory* for trustworthy automatic judging.  
- **Few‑shot + CoT** boosts judge accuracy on reasoning tasks but raises latency / cost.  
- **Human‑parity** benchmarks should always report both raw accuracy *and* bias metrics.

---

## 6 Open Questions

1. Can open‑source judges (e.g., Qwen‑2.5) reach similar agreement with cheaper inference?  
2. How to audit *reasoning correctness* without ballooning evaluation cost?  
3. Will position & verbosity biases worsen as answers get longer (e.g., agent transcripts)?

---

### Image Placeholder

*Add the MT‑Bench experimental flow diagram here once the PNG is available (e.g., `images/mtbench_flow.png`).*

---

**End of notes**

