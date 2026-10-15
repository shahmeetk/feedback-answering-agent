import unittest

from feedback_agent import build_prompt, validate_request


class FeedbackAgentTests(unittest.TestCase):
    def request(self):
        return {
            "subject_type": "service",
            "subject_name": "Example support service",
            "sentiment": "positive",
            "questions": ["How was your experience?"],
            "observations": ["The issue was resolved during the call."],
        }

    def test_valid_request(self):
        self.assertEqual(
            validate_request(self.request())["sentiment"], "positive"
        )

    def test_invalid_sentiment(self):
        data = self.request()
        data["sentiment"] = "invent_praise"
        with self.assertRaises(ValueError):
            validate_request(data)

    def test_questions_or_url_required(self):
        data = self.request()
        del data["questions"]
        with self.assertRaises(ValueError):
            validate_request(data)

    def test_url_only_supported(self):
        data = self.request()
        del data["questions"]
        data["survey_url"] = "https://example.com/survey"
        validate_request(data)

    def test_invalid_observations(self):
        data = self.request()
        data["observations"] = "not a list"
        with self.assertRaises(ValueError):
            validate_request(data)

    def test_all_sentiments_supported(self):
        for sentiment in (
            "positive", "negative", "moderate",
            "extremely_happy", "extremely_sad",
        ):
            data = self.request()
            data["sentiment"] = sentiment
            validate_request(data)

    def test_prompt_contains_policy_and_payload(self):
        prompt = build_prompt(self.request())
        self.assertIn("Sentiment changes emphasis", prompt)
        self.assertIn("Example support service", prompt)


if __name__ == "__main__":
    unittest.main()
