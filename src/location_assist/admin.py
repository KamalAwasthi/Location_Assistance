from django.contrib import admin
from .models import SaveSettings,Live,Reminder

admin.site.register(SaveSettings)
admin.site.register(Live)
admin.site.register(Reminder)