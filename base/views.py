from typing import Any, List
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from typing import List, Dict, Any
# Create your views here.

rooms: List[Dict[Any, Any]] = [
    {
        'id': 0,
        'name': 'Let\'s learn python!'
    },
    {
        'id': 1,
        'name': 'Design with me'
    },
    {
        'id': 2,
        'name': 'Frontend developers'
    }
]


def home(request: HttpRequest) -> HttpResponse:
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request: HttpRequest, pk: str) -> HttpResponse:
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)
