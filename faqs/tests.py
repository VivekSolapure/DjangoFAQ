from django.test import TestCase
from .models import FAQ

class FAQModelTest(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a web framework for Python."
        )

    def test_translation(self):
        self.assertEqual(self.faq.get_translated_question('hi'), self.faq.question_hi)
        self.assertEqual(self.faq.get_translated_answer('hi'), self.faq.answer_hi)

class FAQAPITest(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a web framework for Python."
        )

    def test_api_response(self):
        response = self.client.get('/api/faqs/?lang=hi')
        self.assertEqual(response.status_code, 200)