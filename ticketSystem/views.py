from django.shortcuts import render

from django.http import HttpResponse , request 

#improt json
import json

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def signup(request):
    print(request.method)
    if request.method=="POST":
        body = request.body.decode('utf-8')
        
        return render(request , 'signup.html' , context={'error':''})
    elif(request.method=="GET"):
        print("GET")
        
        return render(request , 'signup.html' , context={})  
    else:
        return render(request , 'templates/signup.html')
