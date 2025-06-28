
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.views import APIView
from django.utils import timezone


class SiteMap(APIView):
    def get(self, request):


        langs = ['en', 'ru', '']


        # Service'lar uchun URL'larni yaratish


        domen = ['https://yurtim.com/ru', 'https://yurtim.com/en', 'https://yurtim.com']

        statical_urls = []
        static_pages = ['products']  # Qo'shmoqchi bo'lgan statik sahifalar
        for page in static_pages:
            for lang in langs:
                if lang:
                    statical_urls.append(f"https://yurtim.com/{lang}/{page}")
                else:
                    statical_urls.append(f"https://yurtim.com/{page}")

        # Barcha URL'larni birlashtirish
        all_urls = domen +  statical_urls

        # XML faylni yaratish
        xml_content = self.generate_sitemap_xml(all_urls)

        # Javobni XML sifatida qaytarish
        return HttpResponse(xml_content, content_type='application/xml')

    def generate_sitemap_xml(self, urls):
        # XML bosh qismi
        xml = ['<?xml version="1.0" encoding="UTF-8"?>']
        xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

        # Har bir URL uchun XML element yaratish
        for url in urls:
            xml.append('<url>')
            xml.append(f'<loc>{url}</loc>')
            xml.append(f'<lastmod>{timezone.now().strftime("%Y-%m-%d")}</lastmod>')  # Oxirgi yangilanish sanasi
            xml.append('<changefreq>daily</changefreq>')  # O'zgarish tezligi
            xml.append('<priority>0.5</priority>')  # Prioritet
            xml.append('</url>')

        # XML oxirini yopish
        xml.append('</urlset>')

        # Barcha XML elementlarini birlashtirib qaytarish
        return '\n'.join(xml)


from django.http import FileResponse
import os


def robots_txt(request):
    # Fayl yo'lini aniqlash
    robots_file_path = os.path.join(os.path.dirname(__file__), 'robots.txt')

    # Faylni ochish va response sifatida yuborish
    try:
        return FileResponse(open(robots_file_path, 'rb'), content_type='text/plain')
    except FileNotFoundError:
        return HttpResponse("Fayl topilmadi", status=404)