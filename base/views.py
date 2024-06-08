from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Home (request):
    return render(request,'home.html') 

def room(request):
    return render(request,'room.html')
