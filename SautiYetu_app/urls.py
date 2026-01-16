from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('technology/', views.technology, name="technology"),
    # Updated path to 'about-us' to match your preferred URL structure
    path('about-us/', views.about, name="about_us"), 
    path('chatbot-response/', views.chatbot_response, name='chatbot_response'),
]