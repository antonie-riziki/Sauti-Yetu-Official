from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.home, name="home"),
    path('projects/', views.projects, name="projects"),
    path('technology/', views.technology, name="technology"),
    path('contact/', views.contact, name="contact"),
    path('chatbot-response/', views.chatbot_response, name='chatbot_response'),

]