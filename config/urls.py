from django.contrib import admin
from django.conf.urls.static import static

from main.sitemap.sitemap import SiteMap, robots_txt
from . import settings
from django.urls import path, include
from config.custom_config import schema_view

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('robots.txt', robots_txt, name='robots'),
                  path('sitemap.xml', SiteMap.as_view(), name='sitemap'),
                  path('api/', include([
                      path('v1/', include('main.urls')),
                      path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  ])),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)