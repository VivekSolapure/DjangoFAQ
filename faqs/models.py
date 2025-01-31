from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)
    question_mr = models.TextField(blank=True, null=True)
    answer_hi = RichTextField(blank=True, null=True)
    answer_mr = RichTextField(blank=True, null=True)

    def get_translated_question(self, lang):
        if lang == 'hi':
            return self.question_hi or self.question
        elif lang == 'mr':
            return self.question_mr or self.question
        return self.question

    def get_translated_answer(self, lang):
        if lang == 'hi':
            return self.answer_hi or self.answer
        elif lang == 'mr':
            return self.answer_mr or self.answer
        return self.answer

    def save(self, *args, **kwargs):
        translator = Translator()
        if not self.question_hi:
            self.question_hi = translator.translate(self.question, dest='hi').text
        if not self.question_mr:
            self.question_mr = translator.translate(self.question, dest='mr').text
        if not self.answer_hi:
            self.answer_hi = translator.translate(self.answer, dest='hi').text
        if not self.answer_mr:
            self.answer_mr = translator.translate(self.answer, dest='mr').text
        super().save(*args, **kwargs)

    def __str__(self):
        return self.question