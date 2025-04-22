from django.contrib import admin
from django.urls import path
from . import views

# from meraproject.myapp import views

urlpatterns = [
    # path('admin/', admin.site.urls), 
    path('',views.home,name='home'),
    path('login_view/',views.login_view,name="login_view"),
    path('login_completed/' ,views.login_completed,name="login_completed"),
    path('register_view/', views.register_view, name='register_view'),
    path('register_complete/',views.register_complete,name="register_complete"),
    path('logout/', views.logout_view, name='logout_view'),
]