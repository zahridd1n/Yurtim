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

class ContactOurSerializer(serializers.ModelSerializer, GeneralMixin):
    address = serializers.SerializerMethodField()
    class Meta:
        model = contact.ContactOur
        fields = ('id', 'address', 'phone', 'email', 'latitude', 'longitude')

    def get_address(self, obj):
        return self.get_translated_field(obj, 'address')

class CategorySerializer(serializers.ModelSerializer, GeneralMixin):
    name = serializers.SerializerMethodField()
    class Meta:
        model = product.Category
        fields = ('id', 'name')

    def get_name(self, obj):
        return self.get_translated_field(obj, 'name')

class ProductSerializer(serializers.ModelSerializer, GeneralMixin):
    name = serializers.SerializerMethodField()
    class Meta:
        model = product.Product
        fields = ('id', 'name', 'category', 'image', 'volume', 'price')

    def get_name(self, obj):
        return self.get_translated_field(obj, 'name')


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = contact.SocialMedia
        fields = ('id', 'name', 'icon', 'link')