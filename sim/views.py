from datetime import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse, StreamingHttpResponse
from .models import Message
import json
import random


def lobby(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if username:
            request.session['username'] = username
        else:
            names = [
                "Horatio", "Benvolio", "Mercutio","Lysander","Demetrius","Sebastian", "Orsino",
                "Malvolio","Hero","Bianca","Gratiano","Feste","Antonio","Lucius","Puck","Lucio",
                "Goneril","Edgar","Edmund", "Oswald"
            ]
            request.session['username'] = f"{random.choice(names)}{datetime.now().timestamp()}"
        print('REady to redorect')
        return redirect('chat')
    else:
        return render(request, 'lobby.html')


def chat(request):
    if not request.session.get('username'):
        return redirect('lobby')
    return render(request, 'chat.html')


def send_chat_message(request):
    content = request.POST.get('content')
    if content:
        Message.objects.create(author=request.sessions["username"], content=content)
    return HttpResponse(status=204)


async def stream_chat_messages(request):

    async def event_stream():
        # Send all existing messages first
        async for message in Message.objects.all().order_by('created_at').values():
            yield f"data: {json.dumps(message)}\n\n"

        last_message = await Message.objects.all().alast()
        if last_message:
            last_id = last_message.id
        else:
            last_id = 0
        
        # Continuously check for new messages
        while True:
            new_messages = Message.objects.filter(id__gt=last_id).values()
            async for message in new_messages:
                yield f"data: {json.dumps(message)}\n\n"
                last_id = message['id']

    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')