from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ChatRoom, Message
from django.contrib.auth.models import User
from django.contrib import messages

@login_required
def admin_chat_room(request):
    if request.user.is_superuser:
        chat_rooms = ChatRoom.objects.all()
    else:
        chat_rooms = ChatRoom.objects.filter(owner=request.user)
    context = {
        'chat_rooms': chat_rooms,
    }
    return render(request, 'chat/admin_chat_room.html', context)

@login_required
def admin_chat_with_user(request, room_id):
    if not request.user.is_superuser:
        return redirect('login')

    chat_room = get_object_or_404(ChatRoom, id=room_id)
    messages = chat_room.messages.order_by('timestamp')
    if request.method == 'POST':
        content = request.POST.get('content')
        Message.objects.create(room=chat_room, sender=request.user, content=content)
        return redirect('admin_chat_with_user', room_id=room_id)

    return render(request, 'chat/admin_chat_with_user.html', {'chat_room': chat_room, 'messages': messages})

@login_required
def user_chat_rooms(request):
    try:
        user = User.objects.get(user=request.user)
    except User.DoesNotExist:
        messages.error(request, 'User profile does not exist. Please contact support.')
        return redirect('logout')

    user_rooms = ChatRoom.objects.filter(user=request.user)
    context = {
        'user_profile': user,
        'user_rooms': user_rooms,
    }
    return render(request, 'chat/user_chat_rooms.html', context)

@login_required
def chat_room(request, room_id):
    print(request.user)
    room = get_object_or_404(ChatRoom, id=room_id, user=request.user)
    messages = room.messages.order_by('timestamp')
    context = {
        'room': room,
        'messages': messages,
    }
    return render(request, 'chat/chat_room.html', context)

@login_required
def send_message(request, room_id):
    if request.method == 'POST':
        content = request.POST.get('content')
        sender = request.user
        room = get_object_or_404(ChatRoom, id=room_id, user=request.user)
        message = Message.objects.create(room=room, sender=sender, content=content)
        return redirect('chat_room', room_id=room_id)
    return redirect('chat_room', room_id=room_id)

@login_required
def send_admin_message(request, user_id):
    if request.method == 'POST':
        content = request.POST.get('content')
        sender = request.user
        user = get_object_or_404(User, id=user_id)
        chat_room, created = ChatRoom.objects.get_or_create(owner=request.user, user=user)
        message = Message.objects.create(room=chat_room, sender=sender, content=content)
        return redirect('admin_chat_with_user', room_id=chat_room.id)
    return redirect('admin_chat_room')
