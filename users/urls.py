"""為應用程序 users 定議url模式"""
from django.urls import path, include
from . import views
app_name ='users'
urlpatterns = [
	path('', include('django.contrib.auth.urls')),
	path('register/', views.register, name='register'),
	]