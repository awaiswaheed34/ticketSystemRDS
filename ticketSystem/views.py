from django.shortcuts import render
#import csrf_exempt 
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse, JsonResponse , request  , response

#improt json
import json
#add cursor
import sqlite3 
from .db import DB
db = DB()
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def signup(request):
    print(request.body)
    if request.method=="POST":
        body = request.POST
        print(body)
        if db.emailExists(body['email']):
            return render(request , 'signup.html' , context={'error':'Email already exists'})
        else:
            db.addUser(body['email'] , body['fname'] , body['lname'] , body['phone'] , body['password'])
            return render(request , 'showAll.html' , context={'success':'Account created successfully'})
          
    elif(request.method=="GET"):
       
        
        return render(request , 'signup.html' , context={})  
    else:
        return render(request , 'templates/signup.html')

def showAll(request):
    rows = db.showAllUsers()
    
    #convert rows into json
    print(rows)
    return render(request , 'showAll.html' , context={'users':rows})