from django.contrib import admin
from django.urls import path
from rest_framework import routers
#from rest.views import TaskSerializerView
from rest.views import add_task, retrieve_task, delete_task, single_retrieve_task, modify_task

# router = routers.DefaultRouter()
# router.register('tasks', TaskSerializerView)


urlpatterns = [ 
    path('tasks/add/', add_task, name="add_task"),
    path('tasks/', retrieve_task, name="retrieve_task"),
    path('tasks/delete/<int:id>/', delete_task, name="delete_task"),
    path('tasks/modify/<int:id>/', modify_task, name="modify_task"),
    path('tasks/<int:id>/', single_retrieve_task, name="single_retrieve_task"),
   


]


