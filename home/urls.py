from atexit import register
from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name="home"),
    path("booking",views.booking,name="booking"),
    path("status",views.status,name="status"),
    path("login",views.login_user,name="login"),
    path("register",views.register,name="register"),
    path("logout",views.logout_user,name="logout"),
    
]