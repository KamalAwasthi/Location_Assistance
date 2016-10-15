from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^location$', views.testview,name= 'testview'),
    url(r'^location/registration$', views.register,name= 'register_view'),
    url(r'^location/login$', views.login,name= 'login_view'),
    url(r'^location/set_settings$', views.set_settings,name= 'set_settings_view'),
    url(r'^location/delete_settings$', views.delete_settings,name= 'delete_settings_view'),
    url(r'^location/set_status$', views.get_live,name= 'set_status_view'),
]