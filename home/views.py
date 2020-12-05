from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    """
    This is page 'home/'
    :param request: output 'Hello world!'
    :return: Hello world
    """
    return HttpResponse('<h1>Hello world!</h1>')


def main_page(request):
    """
    This is main page '/'
    :param request: output 'Hello, this is a home page :)'
    :return: Hello, this is a home page :)
    """
    return render(request, 'index.html')
