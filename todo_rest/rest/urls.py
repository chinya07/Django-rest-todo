from django.contrib import admin
from django.urls import path
from rest_framework import routers
from rest.views import TaskSerializerView

router = routers.DefaultRouter()
router.register('tasks', TaskSerializerView)


urlpatterns = router.urls