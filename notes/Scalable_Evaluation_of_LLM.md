# Week 1 · Day 2 – Lecture Notes: **Evaluating LLMs**

> _Stanford CS25 “Evaluation” mini‑lecture • Last updated 23 Jun 2025_

---

## 📚 Primary Resources

- 📺 **Lecture video:** [ZaQYM‑YF1rM](https://www.youtube.com/watch?v=ZaQYM-YF1rM)
- 📄 Gu et al., 2023 — “Judging LLM‑as‑a‑Judge with MT‑Bench & Chatbot Arena” <https://arxiv.org/abs/2306.05685>
- 📄 Zhang et al., 2025 — “A Survey on LLM‑as‑a‑Judge” <https://arxiv.org/abs/2411.15594>

---

## 1  Why Evaluation Matters

> **Goal:** Quantify progress so you can…
>
> 1. **Identify improvements**
> 2. **Select models** for a use‑case
> 3. **Decide production readiness**

> 💭 **How does this differ from non‑LLM software QA?**  
> Traditional apps have binary pass/fail specs; generative models live on a quality continuum, so we need graded metrics and statistical tests.

### 🛠️ Core ingredients of any evaluation pipeline

- **Evaluation dataset** (prompts/instructions + references)  
- **Evaluation metric** (automatic, human, or hybrid)

### Classic ML example

> Dog‑vs‑not‑dog classifier ⇒ closed‑ended, single scalar accuracy.

---

## 2  Evaluation Challenges with LLMs

| Challenge | Why it’s hard | Typical work‑around |
|-----------|---------------|---------------------|
| 🌐 **Task diversity & open‑endedness** | No single “ground‑truth” answer | Collect *many* representative prompts or convert to closed questions (but that may change the task). |
| 🔍 **Reference‑based metrics too rigid** | BLEU/ROUGE struggle with creative tasks (“Write me a book”). | Use semantic similarity or human/LLM judges. |
| 👩‍⚖️ **Human evaluation** | Accurate but expensive, slow, non‑reproducible. | **LLM‑as‑a‑Judge**: delegate scoring to a strong model. |

### Papers studying LLM judges

- **Zhang 2025** – comprehensive survey  
- **Gu 2023** – MT‑Bench, Arena agreement  
- **Sun 2024** – “Prometheus” fine‑tuned judge <https://arxiv.org/abs/2404.04475>

---

## 3  Academic & Open Benchmarks

### High‑level purposes

- **Development loop** (quick regression tests)  
- **Model selection & leaderboard PR**  
- **Public accountability**

### Metric note – *Perplexity*

- Intuition: average branching factor over tokens.  
- ⚠️ Not comparable across tokenizers or corpora → best used *within* one model family.

### “Kitchen‑sink” closed‑task suites

- **HELM**, **HF Open LLM Leaderboard v2**  
  - *MMLU‑Pro*: broad knowledge  
  - *GPQA*: expert‑level questions  
  - *MuSR*: long‑context reasoning  
  - *MATH*: high‑school math  
  - *IFEval*: instruction‑following format check  
  - *BBH*: 23 challenge tasks

> **Pros:** simple, one‑number score.  
> **Cons:** weak on open‑ended generation.

### Human‑in‑the‑loop leaderboards

- **Chatbot Arena** – pairwise Elo from crowd votes.

### LLM‑based leaderboards

- **AlpacaEval / AlpacaEval‑LC**  
  - Graphic in lecture: cost vs. agreement with humans → LLM judges reach **94 %** correlation (post‑length‑control **98 %**).

---

## 4  LLM‑as‑a‑Judge: Pros, Cons & Biases

### ✅ Benefits

- Handles **open‑ended** tasks  
- **Scales** cheaply & quickly  
- Quality improves with stronger backbone models

### ⚠️ Drawbacks

- Requires **trust** in the “oracle” LLM  
- Potential **biases** & *spurious correlations* (e.g., length, style)  
- Some loss of manual **control / interpretability**

#### Observed biases & mitigations

| Bias | Observation | Mitigation |
|------|-------------|------------|
| **Length bias** | AlpacaEval 1.0: longer answers won **74 %** of comparisons. | Regression debiasing → AlpacaEval 2.0. |
| **Position bias** | Judges favour left/first answer. | Randomised answer order. |
| **Verbosity / self‑identification** | Judges reward model self‑praise. | Strip model IDs & enforce length cap. |

---

## 5  Specialised Benchmarks & Tools

- **MT‑Bench** – multi‑turn dialogue quality.  
- **RubricEval** – scalable scoring in expert domains.

> Other open issues: data contamination, benchmark monoculture, adversarial robustness.

---

## 6  Take‑home Questions

1. Which bias matters *most* for your use‑case, and how will you detect it?  
2. If GPT‑4o is the judge, how do you quantify drift when GPT‑5 arrives?  
3. Where does human evaluation still provide irreplaceable value?

---

**End of notes**

