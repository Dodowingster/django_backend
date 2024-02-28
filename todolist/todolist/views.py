from django.shortcuts import render
from .models import task
from .serializers import TaskSerializer
from rest_framework import generics

# Create your views here.
class TaskListCreate(generics.ListCreateAPIView):
    queryset = task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = task.objects.all()
    serializer_class = TaskSerializer