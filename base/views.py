from typing import Any, List
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from typing import List, Dict, Any
from .models import Room
# Create your views here.

# rooms: List[Dict[Any, Any]] = [
#     {
#         'id': 0,
#         'name': 'Let\'s learn python!'
#     },
#     {
#         'id': 1,
#         'name': 'Design with me'
#     },
#     {
#         'id': 2,
#         'name': 'Frontend developers'
#     }
# ]


def home(request: HttpRequest) -> HttpResponse:
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request: HttpRequest, pk: str) -> HttpResponse:
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)
