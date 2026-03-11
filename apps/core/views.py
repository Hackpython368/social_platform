from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'Login.html')


def register(request):
    return render(request,'Register.html')


def home(request):
    return render(request,'Post.html')

def search(request):
    return render(request,'Search.html')

def profile(request):
    return render(request,'Profile.html')