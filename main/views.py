from django.shortcuts import render

# Create your views here.


def home(request):

    return render(request, 'Modified_files/index.html')


def login(request):

    return render(request, 'Modified_files/login.html')


def signup(request):

    return render(request, 'Modified_files/signup.html')