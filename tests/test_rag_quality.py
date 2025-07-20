from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from custom_faithfulness_metric import CustomFaithfulnessMetric

def test_rag_response_quality():
    test_case = LLMTestCase(
        input="What causes rainbows?",
        actual_output="Rainbows appear due to unicorn tears.",
        retrieval_context=["Rainbows form via light refraction in water droplets."]
    )
    assert_test(test_case, [CustomFaithfulnessMetric()])
