from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect
from .models import SaveSettings,Live
import json

# Create your views here
#views for user table
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


#views for save_settings table
@csrf_exempt
def set_settings(request):
    current_username=request.POST.get('username')
    current_longitude = request.POST.get('longitude')
    current_latitude = request.POST.get('latitude')
    current_volumeLevel = request.POST.get('volumeLevel')
    current_vibrationMode = request.POST.get('vibrationMode')
    current_brightness = request.POST.get('brightness')
    current_mobileData = request.POST.get('mobileData')
    current_wifi = request.POST.get('wifi')
    current_bluetooth = request.POST.get('bluetooth')
    current_activity = request.POST.get('activity')
    try:
        user=User.objects.get(username=current_username)
    except Exception as e:
        return HttpResponse("username is not registered")

    try:
        settings = SaveSettings(longitude = current_longitude, latitude = current_latitude, volumeLevel = current_volumeLevel, vibrationMode = current_vibrationMode, 
        brightness = current_brightness, mobileData = current_mobileData, wifi = current_wifi, bluetooth = current_bluetooth, activity = current_activity)
        settings.save()
    except Exception as e:
        return HttpResponse("error in user input")

    return HttpResponse("Settings saved")  


@csrf_exempt
def delete_settings(request):
    current_username = request.POST.get('username')
    current_longitude = request.POST.get('longitude')
    current_latitude = request.POST.get('latitude')
    try:
        user=User.objects.get(username=current_username)
    except Exception as e:
        return HttpResponse("username is not registered")

    user = User.objects.get(username = current_username)
    setting = SaveSettings.objects.get(longitude = current_longitude)   
    setting = SaveSettings.objects.get(latitude = current_latitude)  
    
    setting.delete()

    return HttpResponse("settings successfully deleted") 



#Live Model views

@csrf_exempt
def get_live(request):
    current_username = request.POST.get('username')
    current_longitude = request.POST.get('longitude')
    current_latitude = request.POST.get('latitude')
    current_time = request.POST.get('time')

    try:
        user=User.objects.get(username=current_username)
    except Exception as e:
        return HttpResponse("username is not registered")

    live_status = Live(username = current_username, longitude = current_longitude, 
        latitude = current_latitude, time = current_time)
    live_status.save()

    return HttpResponse("live status recorded")


