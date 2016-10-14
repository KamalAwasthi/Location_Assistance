from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^location$', views.testview,name= 'testview'),
    url(r'^location/registration$', views.register,name= 'register_view'),
    url(r'^location/login$', views.login,name= 'login_view'),
]