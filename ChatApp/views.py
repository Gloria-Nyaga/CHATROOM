from django.shortcuts import render, redirect
from .models import Room, Message
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def Create_Room(request):
    if request.method == 'POST':
        room_name = request.POST.get('room')
        if room_name:
            room, created = Room.objects.get_or_create(room_name=room_name)
            return redirect('messages', room_name=room_name)  # Redirect to the chat room
    return render(request, 'index.html')

@login_required
def Message_View(request, room_name):
    room = Room.objects.get(room_name=room_name)

    if request.method == 'POST':
        message_content = request.POST.get('message')
        if message_content:
            # Create a new message in the room
            new_message = Message.objects.create(
                room=room,
                sender=request.user,  # The currently logged-in user
                message=message_content
            )
            new_message.save()
            return redirect('messages', room_name=room_name)  # Redirect to the same room

    messages = Message.objects.filter(room=room).order_by('-timestamp')  # Assuming you have a timestamp field
    return render(request, 'message.html', {
        'room_name': room_name,
        'messages': messages,
        'user': request.user.username
    })

def Login_View(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to the room creation page
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

def Index_View(request):
    return render(request, 'index.html')
