from django.urls import path
from .views import *

urlpatterns = [
    path('images/', ImageView.as_view()),
    path('faq/<str:lang>/', FAQView.as_view()),
    path('send-message/', SendMessage.as_view()),
    path('contact-our/<str:lang>/', ContactOurView.as_view()),
    path('social-media/', SocialMediaView.as_view()),
    path('category/<str:lang>/', CategoryView.as_view()),
    path('product/<str:lang>/', ProductView.as_view()),
]