from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect
from .models import SaveSettings,Live, Reminder,FriendList
from django.core import serializers
import json
import unicodedata

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


@csrf_exempt
def search(request):
    current_username=request.POST.get('username')
    try:
        user=User.objects.get(username=current_username)
        python_object = {'flag':'True',
                        'userName': user.username,
                        'first_name': user.first_name,
                        'last_name': user.last_name}
    except Exception as e:
        python_object = {'flag':'False'}
    datatosend=json.JSONEncoder().encode(python_object)
    return HttpResponse(datatosend)

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
        settings.username =user
        settings.save()
    except Exception as e:
        return HttpResponse("error in user input")

    return HttpResponse("Settings saved")  

@csrf_exempt
def sync_settings(request):
    current_username=str(request.POST.get('username'))
    current_username=str(current_username)
    try:
        user=User.objects.get(username=current_username)
    except Exception as e:
        return HttpResponse("username is not registered")

    queryset = SaveSettings.objects.filter(username__username = current_username)
    queryset=serializers.serialize('json',queryset)
    return HttpResponse(queryset)

    


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

    try:
        live_status = Live.objects.get(username__username = current_username)
        live_status.longitude = current_longitude
        live_status.latitude = current_latitude
        live_status.time = current_time
        live_status.save()
    except:
        live_status = Live(username = user, longitude = current_longitude, 
            latitude = current_latitude, time = current_time)
        live_status.save()

    return HttpResponse("live status recorded")

#views for Reminder TABLE

@csrf_exempt
def set_reminder(request):
    current_username = request.POST.get('username')
    current_longitude = request.POST.get('longitude')
    current_latitude = request.POST.get('latitude')
    current_reminder_title = request.POST.get('reminder_title')    
    current_reminder_text = request.POST.get('reminder_text')

    try:
        user=User.objects.get(username=current_username)
    except Exception as e:
        return HttpResponse("username is not registered")

    reminder = Reminder(username = user, longitude = current_longitude, 
        latitude = current_latitude, reminder_title = current_reminder_title, reminder_text = current_reminder_text)
    reminder.save()

    return HttpResponse("reminder has been set")

@csrf_exempt
def sync_reminders(request):
    current_username=str(request.POST.get('username'))
    current_username=str(current_username)
    try:
        user=User.objects.get(username=current_username)
    except Exception as e:
        return HttpResponse("username is not registered")

    queryset = Reminder.objects.filter(username__username = current_username)
    queryset=serializers.serialize('json',queryset)
    return HttpResponse(queryset)

@csrf_exempt
def delete_reminder(request):
    current_username = request.POST.get('username')
    reminder_id = request.POST.get('id')

    try:
        user=User.objects.get(username=current_username)
    except Exception as e:
        return HttpResponse("username is not registered")
        #setting = SaveSettings.objects.get(latitude = current_latitude) 
    deleted_reminder = Reminder.objects.get(pk = reminder_id)

    deleted_reminder.delete()

    return HttpResponse("reminder deleted sucessfully")


#Friends Table View
@csrf_exempt
def add_friends(request):
    current_username = request.POST.get('username')
    current_friendList = request.POST.get('friendList')
    try:
        username=User.objects.get(username=current_username)
    except Exception as e:
        status = 203
        return HttpResponse(status)
    json_obj = json.loads(current_friendList)
    ol=[]
    try:
        existingUser = FriendList.objects.get(user__username = username)
        user_friends = existingUser.getfoo()
        for c in user_friends:
            c = unicodedata.normalize('NFKD', c).encode('ascii','ignore')
            # print type(c)
            ol.append(c)
        for c in json_obj:
            c = unicodedata.normalize('NFKD', c).encode('ascii','ignore')
            ol.append(c)
        existingUser.friendList = json.dumps(ol)
        existingUser.save()
        status = 100
    except:
        friend = FriendList(user = username)
        friend.setfoo(current_friendList) 
        friend.save()
        status = 200
    return HttpResponse(status)

@csrf_exempt
def check_friendship(request):
    current_username = request.POST.get('selfUsername')
    current_friendName = request.POST.get('friendUsername')
    # try:
    #     selfusername=User.objects.get(username=current_username)
    # except Exception as e:
    #     python_object = {'user':'False',
    #                     'frienduser':'False'}
    #     datatosend=json.JSONEncoder().encode(python_object)
    #     return HttpResponse(datatosend)

    try:
        friendusername=User.objects.get(username=current_friendName)
    except Exception as e:
        python_object = {'user':'True',
                        'frienduser':'False'}
        datatosend=json.JSONEncoder().encode(python_object)
        return HttpResponse(datatosend)
    
    try:
        friend = False
        existingUser = FriendList.objects.get(user__username = current_username)
        user_friends = existingUser.getfoo()
        for c in user_friends:
            c = unicodedata.normalize('NFKD', c).encode('ascii','ignore')
            if(c == current_friendName):
                friend = True
                break;
        if(friend == True):
            try:
                live_user = Live.objects.get(username__username = current_friendName)
            except Exception as e:
                python_object = {'user':'True',
                                'frienduser':'True',
                                'live_status':'false',
                                'friend':'True'}
                datatosend = json.JSONEncoder().encode(python_object)
                return HttpResponse(datatosend)
            ff_latitude = live_user.latitude
            ff_longitude = live_user.longitude
            python_object = {'user':'True',
                            'frienduser':'True',
                            'live_status':'True',
                            'latitude':str(ff_latitude),
                            'longitude':str(ff_longitude),
                            'friend':'True'}
        else:
            python_object = {'user':'True',
                            'frienduser':'True',
                            'friend':'False'}
    except:
        python_object = {'user':'True',
                        'frienduser':'True'}
    datatosend=json.JSONEncoder().encode(python_object)
    return HttpResponse(datatosend)

# @csrf_exempt
# def delete_friends(request):
#     current_username = request.POST.get('username')
#     current_friendList = request.POST.get('friendList')
#     try:
#         username=User.objects.get(username=current_username)
#     except Exception as e:
#         return HttpResponse("username is not registered")
#     json_obj = json.loads(current_friendList)
#     ol=[]
#     try:
#         existingUser = FriendList.objects.get(user__username = username)
#         user_friends = existingUser.getfoo()
#         for c in json_obj:
#             c = unicodedata.normalize('NFKD', c).encode('ascii','ignore')
#             ol.append(c)
#         existingUser.friendList = ol
#         existingUser.save()
#     except:
#         friend = FriendList(user = username)
#         friend.setfoo(current_friendList) 
#         friend.save()
#     return HttpResponse(str(ol))

@csrf_exempt
def get_friends(request):
    current_username = request.POST.get('username')
    ol=[]
    try:
        existingUser = FriendList.objects.get(user__username = current_username)
        user_friends = existingUser.getfoo()
        for c in user_friends:
            c = unicodedata.normalize('NFKD', c).encode('ascii','ignore')
            ol.append(c)
    except:
        ol=[]
    return HttpResponse(json.dumps(ol))




