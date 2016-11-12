from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^location$', views.testview,name= 'testview'),
    url(r'^location/registration$', views.register,name= 'register_view'),
    url(r'^location/login$', views.login,name= 'login_view'),
    url(r'^location/search_user$', views.search,name= 'search_view'),
    url(r'^location/set_settings$', views.set_settings,name= 'set_settings_view'),
    url(r'^location/sync_settings$', views.sync_settings,name= 'sync_settings_view'),
    url(r'^location/delete_settings$', views.delete_settings,name= 'delete_settings_view'),
    url(r'^location/set_status$', views.get_live,name= 'set_status_view'),
    url(r'^location/set_reminder$', views.set_reminder,name= 'set_reminder_view'),
    url(r'^location/sync_reminders$', views.sync_reminders,name= 'sync_reminders_view'),
    url(r'^location/delete_reminder$', views.delete_reminder,name= 'delete_reminder_view'),
    url(r'^location/add_friends$', views.add_friends,name= 'add_friends_view'),
]