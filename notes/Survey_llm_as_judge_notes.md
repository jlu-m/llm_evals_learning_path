# Week 1 · Day 2 — Paper Notes: **“A Survey on LLM‑as‑a‑Judge”**

*Zhang et al., March 2025 ― *[*https://arxiv.org/abs/2411.15594*](https://arxiv.org/abs/2411.15594)

---

## 1 What is “LLM‑as‑a‑Judge”?

> An **umbrella term** for large‑language‑model evaluators that *score, rank, or verify* outputs from other models.
>
> **Spectrum of roles**\
> – *Graders* • *Assessors* • *Critics* • *Verifiers* • *Examiners* • *Reward / ranking models*

---

## 2 End‑to‑End Evaluation Pipeline

```
Input  ⇒  In‑Context Learning  ⇒  Model Selection  ⇒  Post‑Processing  ⇒  Evaluation
```



*Replace the placeholder above with the lecture slide (image ID 23dac52e…).*

---

## 3 Choosing the Backbone Judge

| Category                    | Example                                                                  | Notes                                                               |
| --------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------- |
| **Proprietary**             | **GPT‑4**                                                                | Highest agreement with pro human judges, but privacy & cost issues. |
| **Open‑source, fine‑tuned** | **PandaLM** (LLaMA‑7B), **JudgeLM** (Vicuna), **Auto‑J**, **Prometheus** | Cheap & reproducible; still chasing GPT‑4 performance.              |

### Current status (Mar 2025)

- GPT‑4 remains the **de‑facto oracle**.
- Research explores cheaper substitutes; **Qwen‑2.5‑7B‑Instruct** shows promise.

---

## 4 Applications Beyond Model Scoring

- **Data labelling** (automatic reference generation)
- **Agent feedback loops**
- **Reasoning trace checking**

---

## 5 Designing Better Judges

> The survey recommends **explicit scoring dimensions** → higher reliability.

### Improvement Levers

| Layer           | Tactics                                                 |
| --------------- | ------------------------------------------------------- |
| **Prompt**      | Decompose criteria; request explanation‑of‑score.       |
| **LLM ability** | Fine‑tune on evaluation datasets or human feedback.     |
| **Post‑result** | Majority voting, regression debiasing, score smoothing. |

&#x20;*Insert slide image ID 2a37e931… here.*

---

## 6 Evaluating the Evaluators

| Metric family      | Typical stats                            |
| ------------------ | ---------------------------------------- |
| **Agreement**      | % Exact, Cohen’s κ, Spearman ρ           |
| **Classification** | Precision / Recall / F₁ vs. human labels |

### Bias dimensions

*Task‑agnostic* (culture, diversity, self‑enhancement) vs *judgement‑specific*:

- **Position bias** – measured via *position consistency* & *preference fairness*; see *conflict‑rate* metric.
- **Compassion‑fade** – higher scores for GPT‑4‑labelled answers.
- **Style & concreteness** – emoji, authoritative tone, numeric detail.

Benchmarks: **EVALBIASBENCH**, **CALM** (bias quantification toolkit).

---

## 7 Robustness & Security

- **Adversarial prompts** can trick judges (e.g., hidden “praise me” tokens).
- *Null prompts* sometimes pass with high scores — see [https://arxiv.org/abs/2410.07137](https://arxiv.org/abs/2410.07137).

---

## 8 Empirical Findings (LLMEval 2 snapshot)

- **GPT‑4** still wins by a wide margin.
- **Open‑source** Qwen‑2.5‑7B‑Instruct performs best among non‑proprietary.
- All tested LLM judges scored **poorly on bias suites**.

#### Mitigation experiments

| Trick                       | Effect                                  |
| --------------------------- | --------------------------------------- |
| “Answer + explanation”      | ↑ interpretability, ↓ overall accuracy. |
| Self‑validation             | Minimal gains.                          |
| Majority vote (round‑robin) | Clear benefit.                          |
| Mean / best‑score fusion    | No improvement.                         |
| Multi‑LLM voting            | Highly model‑dependent.                 |

---

## 9 Reasoning‑intensive Judging

Models like **gemini‑2.0‑thinking, o1‑mini, o3‑mini, DeepSeek‑R1** approach GPT‑4‑turbo on raw accuracy, but lag in *human‑alignment* tasks.

> **Open question:** How to quantify reasoning‑step correctness at scale?

---

## 10 Interesting Application Spotlight

> **Bug‑report summarisation evaluation** — Shi et al., 2024 [https://arxiv.org/abs/2409.00630](https://arxiv.org/abs/2409.00630)

Demonstrates a domain‑specific judge outperforming general LLMs.

---

## 11 Grand Challenges

1. **Reliability** – Overconfidence, fairness, generalisation gaps.
2. **Robustness** – Adversarial attacks & judge gaming.
3. **Model power** – Multi‑modal judges still struggle.

---

### Quick Reflection Prompts

1. Which *bias metric* (position, compassion‑fade, style) is most critical for your use‑case?
2. If GPT‑5 arrives tomorrow, how would you validate that it remains an unbiased oracle?
3. What would an *ideal* open‑source judge look like for your team?

---

**End of notes**

