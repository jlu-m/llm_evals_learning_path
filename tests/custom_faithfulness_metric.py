from deepeval.metrics.base_metric import BaseMetric
from deepeval.test_case import LLMTestCase
from openai import OpenAI
import os

class CustomFaithfulnessMetric(BaseMetric):
    def __init__(self, threshold=0.7):
        self.threshold = threshold
        self.score = None
        self.reason = ""
        self.async_mode = True
        self.client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    def measure(self, test_case: LLMTestCase):
        prompt = f"""
Evaluate whether the following output is faithful to the given context.

Context:
{test_case.retrieval_context}

Output:
{test_case.actual_output}

Respond with a number from 0 to 1, where 1 = fully faithful and 0 = hallucinated.
"""
        resp = self.client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        self.score = float(resp.choices[0].message.content.strip())
        self.reason = f"Judged score {self.score:.2f} from prompt:\n{prompt[:100]}..."
        return self.score

    def is_successful(self):
        return self.score >= self.threshold

    async def a_measure(self, test_case: LLMTestCase, **kwargs):
        return self.measure(test_case)

    @property
    def metric_name(self):
        return "CustomFaithfulness"
