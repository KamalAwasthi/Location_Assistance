from django.contrib import admin
from .models import SaveSettings,Live,Reminder,FriendList,UserSummary

admin.site.register(SaveSettings)
admin.site.register(Live)
admin.site.register(Reminder)
admin.site.register(FriendList)
admin.site.register(UserSummary)
