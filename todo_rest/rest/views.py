from django.shortcuts import render
#from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

# class TaskSerializerView(viewsets.ModelViewSet):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer   


@api_view(['POST'])
def add_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def retrieve_task(request):
    data = Task.objects.all()
    serializer = TaskSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_task(request, id):
    Task.objects.delete(pk=id)
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def single_retrieve_task(request, id):
    data = Task.objects.get(pk=id)
    serializer = TaskSerializer(data)
    return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['PUT'])
def modify_task(request, id):
    data = Task.objects.get(pk=id) 
    serializer = TaskSerializer(data, request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

