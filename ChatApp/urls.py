from django.urls import path
from . import views

urlpatterns = [
    path('user/chat_rooms/', views.user_chat_rooms, name='user_chat_rooms'),
    path('admin_chat_with_user/<int:room_id>/', views.admin_chat_with_user, name='admin_chat_with_user'),
    path('chat/<int:room_id>/', views.chat_room, name='chat_room'),
    path('send_message/<int:room_id>/', views.send_message, name='send_message'),
    path('send_admin_message/<int:user_id>', views.send_admin_message, name='send_admin_message'),
    path('chat/admin_chat_room/', views.admin_chat_room, name='admin_chat_room')
]