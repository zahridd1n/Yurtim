from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
import requests
import urllib.parse
from config import settings

from main.models import contact, faq, product, base
from main.serializers import ImageSerializer, FAQSerializer, ProductSerializer, CategorySerializer, ContactOurSerializer, SocialMediaSerializer



class ImageView(APIView):
    def get(self, request):
        images_1 = product.ProductImages.objects.all().order_by('?')
        images_2 = product.ProductImages.objects.all().order_by('?')
        serializer_1 = ImageSerializer(images_1, many=True, context={'request': request})
        serializer_2 = ImageSerializer(images_2, many=True, context={'request': request})
        data = {
            'success': True,
            'message': 'Success',
            'data': {
                'images_1': serializer_1.data,
                'images_2': serializer_2.data
            }
        }
        return Response(data, status=status.HTTP_200_OK)


class FAQView(APIView):
    def get(self, request, lang=None):
        faqs = faq.Faq.objects.filter(is_active=True)
        serializer = FAQSerializer(faqs, many=True, context={'lang': lang})
        data = {
            'success': True,
            'message': 'Success',
            'data': serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)


class SendMessage(APIView):
    def post(self, request):
        try:
            name = request.data.get('name')
            phone = request.data.get('phone')
            message = request.data.get('message')

            # Validate input
            if not all([name, phone, message]):
                return Response(
                    {'success': False, 'message': 'All fields (name, phone, message) are required'},
                    status=400
                )

            bot_keys = base.BotKeys.objects.first()
            if not bot_keys:
                return Response(
                    {'success': False, 'message': 'Bot configuration not found'},
                    status=500
                )

            BOT_TOKEN = bot_keys.token
            GROUP_CHAT_ID = bot_keys.chat_id

            text = f"""🆕 Yangi xabar yuborildi:\n
        👤 Yuboruvchi: {name}
        📞 Telefon: {phone}
        ✉️ Xabar: {message}
            """
            encoded_text = urllib.parse.quote_plus(text)

            # Send message to Telegram
            url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={GROUP_CHAT_ID}&text={encoded_text}'
            response = requests.get(url)

            if response.status_code != 200:
                error_message = response.json().get('description', 'Unknown error')
                print(f"Telegram API error: {response.status_code} - {error_message}")
                return Response(
                    {'success': False, 'message': f'Telegram API error: {error_message}'},
                    status=500
                )

            # Save to database
            contact.Contact.objects.create(name=name, phone=phone, message=message)
            return Response({'success': True, 'message': 'Success'})

        except Exception as e:
            print(f"Server error: {str(e)}")
            return Response(
                {'success': False, 'message': f'Server error: {str(e)}'},
                status=500
            )


class CategoryView(APIView):
    def get(self, request, lang=None):
        categories = product.Category.objects.all()
        serializer = CategorySerializer(categories, many=True, context={'lang': lang})
        data = {
            'success': True,
            'message': 'Success',
            'data': serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)


class ContactOurView(APIView):
    def get(self, request, lang=None):
        contact_our = contact.ContactOur.objects.first()
        serializer = ContactOurSerializer(contact_our, context={'lang': lang})
        data = {
            'success': True,
            'message': 'Success',
            'data': serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)


class ProductView(APIView):
    def get(self, request, lang=None):
        category_id = request.query_params.get('category_id')
        if category_id:
            products = product.Product.objects.filter(category_id=category_id)

        else:
            products = product.Product.objects.all()

        serializer = ProductSerializer(products, many=True, context={'lang': lang, "request":request})
        data = {
            'success': True,
            'message': 'Success',
            'data': serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)

class SocialMediaView(APIView):
    def get(self, request):
        social_media = contact.SocialMedia.objects.all()
        serializer = SocialMediaSerializer(social_media, many=True, context={'request': request})
        data = {
            'success': True,
            'message': 'Success',
            'data': serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)