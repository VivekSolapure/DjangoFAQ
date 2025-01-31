from django.core.cache import cache
from rest_framework import viewsets
from .models import FAQ
from .serializers import FAQSerializer

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get_queryset(self):
        lang = self.request.query_params.get('lang', 'en')
        cache_key = f'faqs_{lang}'
        cached_faqs = cache.get(cache_key)

        if cached_faqs:
            return cached_faqs

        faqs = FAQ.objects.all()
        for faq in faqs:
            faq.question = faq.get_translated_question(lang)
            faq.answer = faq.get_translated_answer(lang)

        cache.set(cache_key, faqs, timeout=60 * 15)  # Cache for 15 minutes
        return faqs