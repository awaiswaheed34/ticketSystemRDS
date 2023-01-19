from django.shortcuts import render
#import csrf_exempt 
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse , request  , response

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
    print(request.method)
    if request.method=="POST":
        body = json.loads(request.body.decode('utf-8'))
        if db.emailExists(body['email']):
            return render(request , 'signup.html' , context={'error':'Email already exists'})
        else:
            return response()
          
    elif(request.method=="GET"):
       
        
        return render(request , 'signup.html' , context={})  
    else:
        return render(request , 'templates/signup.html')
