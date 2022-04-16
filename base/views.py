from django.shortcuts import render

# Create your views here.


rooms = [
    {
        'id': 1,
        'name': 'Let\'s learn python'
    },
    {
        'id': 2,
        'name': 'Design with me!'
    },
    {
        'id': 3,
        'name': 'Frontend developers'
    },
]


def home(request):
    # return HttpResponse('Home page')
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    # return HttpResponse('You\'re in rooms!')
    return render(request, 'base/room.html')
