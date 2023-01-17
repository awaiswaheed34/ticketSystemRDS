from django.shortcuts import render

from django.http import HttpResponse , request 
#import request from django.http import request


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def signup(request):
    if request.method=="POST":
        print(request.POST)
        return HttpResponse("CHECK")
    else:
        return render(request , 'signup.html')
