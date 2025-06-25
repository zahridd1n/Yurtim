from django.db import models


class Faq(models.Model):
    question_uz = models.TextField()
    question_ru = models.TextField(null=True, blank=True)
    question_en = models.TextField(null=True, blank=True)
    answer_uz = models.TextField()
    answer_ru = models.TextField(null=True, blank=True)
    answer_en = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.question_uz

    class Meta:
        verbose_name = 'Faq'
        verbose_name_plural = 'Faqs'
