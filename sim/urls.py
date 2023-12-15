from django.urls import path
from . import views

urlpatterns = [
    path('lobby/', views.lobby, name='lobby'),
    path('', views.chat, name='chat'),
    path('send-chat-message/', views.send_chat_message, name='send-chat-message'),
    path('stream-chat-messages/', views.stream_chat_messages, name='stream-chat-messages'),
]