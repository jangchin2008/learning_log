"定義 learning_logs的url模式"
from django.urls import path
from . import views
app_name = 'learning_logs'
urlpatterns = [
 #主頁
 	path('', views.index,name='index'),
 	path('topics/',views.topics,name='topics'),
 	path('topics/<int:topic_id>/', views.topic, name='topic'),
 	#用於加新主題頁面
 	path('new_topic/', views.new_topic, name='new_topic'),
 	path('new_entry/<int:topic_id>/',views.new_entry, name='new_entry'),
 	path('edit_entry/<int:entry_id>/',views.edit_entry, name='edit_entry'),
 	]