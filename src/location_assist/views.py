from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect
import json

# Create your views here.

def testview(request):
	user = User.objects.all()
	userset= serializers.serialize('json',user)
	return render(request,'location/list.html',{'user':user})


@csrf_exempt
def register(request):
    username=request.POST.get('username','')
    password=request.POST.get('password','')
    first_name=request.POST.get('first_name','')
    last_name=request.POST.get('last_name','')
    user=''
    try:
    	user=User.objects.get(username=username)
    except Exception as e:
    	if user is not None:
        	new_user= User.objects.create_user(username, 'example@example.com' ,password )
        	new_user.first_name= first_name
        	new_user.last_name= last_name
        	new_user.save()
    		return HttpResponse("new user registration successful")
    return HttpResponse("username already taken")

@csrf_exempt
def login(request):
    username=request.POST.get('username','')
    password=request.POST.get('password','')
    user=authenticate(username=username,password=password)

    if user is not None:
        return HttpResponse("login successful")
    else:
        return HttpResponse("invalid credentials")