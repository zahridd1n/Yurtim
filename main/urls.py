from django.urls import path
from .views import *

urlpatterns = [
    path('images/', ImageView.as_view()),
    path('faq/', FAQView.as_view()),
]