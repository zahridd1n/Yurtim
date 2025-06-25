from rest_framework import serializers
from main.models import contact, faq, product


class GeneralMixin:
    def get_translated_field(self, obj, field_name):  # Tilga asoslangan maydon qiymatini qaytaruvchi umumiy funksiya
        lang = self.context.get('lang')
        if lang == 'ru':
            return getattr(obj, f"{field_name}_ru")  # Masalan, title_ru qaytariladi
        elif lang == 'en':
            return getattr(obj, f"{field_name}_en")  # Masalan, title_en qaytariladi
        else:
            return getattr(obj, f"{field_name}_uz")  # Masalan, title_uz qaytariladi


class FAQSerializer(serializers.ModelSerializer, GeneralMixin):
    question = serializers.SerializerMethodField()
    answer = serializers.SerializerMethodField()

    class Meta:
        model = faq.Faq
        fields = ('id', 'question', 'answer')

    def get_question(self, obj):
        return self.get_translated_field(obj, 'question')

    def get_answer(self, obj):
        return self.get_translated_field(obj, 'answer')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = product.ProductImages
        fields = ('id', 'image')