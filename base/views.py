from django.shortcuts import render

# Create your views here.


def home(request):
    # return HttpResponse('Home page')
    return render(request, 'home.html')


def room(request):
    # return HttpResponse('You\'re in rooms!')
    return render(request, 'room.html')
