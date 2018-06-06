from django.shortcuts import render
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
# Create your views here.

class TaskSerializerView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer   