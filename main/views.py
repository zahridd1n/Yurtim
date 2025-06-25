from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
import requests
import urllib.parse
from config import settings

from main.models import contact, faq, product
from main.serializers import ImageSerializer, FAQSerializer


class ImageView(generics.ListAPIView):
    serializer_class = ImageSerializer
    queryset = product.ProductImages.objects.all()


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
