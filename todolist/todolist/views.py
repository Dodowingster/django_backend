from django.shortcuts import render
from .models import task
from .serializers import TaskSerializer
from rest_framework import generics

class TaskListCreate(generics.ListCreateAPIView):
    queryset = task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = task.objects.all()
    serializer_class = TaskSerializer

# ______________________________________________________________________________
#                                                                              
#  This code defines two Django REST Framework (DRF) API views for handling    
#  tasks: TaskListCreate and TaskRetrieveUpdateDestroy. These views inherit    
#  from DRF's generic API views, providing built-in functionality for common   
#  CRUD operations (Create, Retrieve, Update, Delete).                        
#                                                                              
#  - The TaskListCreate view is responsible for listing and creating tasks.    
#    It inherits from generics.ListCreateAPIView and automatically generates   
#    endpoints for retrieving a list of tasks (GET request) and creating a new 
#    task (POST request). It specifies the queryset to fetch all tasks from    
#    the database and the TaskSerializer to serialize task data.               
#                                                                              
#  - The TaskRetrieveUpdateDestroy view handles retrieving, updating, and       
#    deleting individual tasks. It inherits from                            
#    generics.RetrieveUpdateDestroyAPIView and provides endpoints for          
#    retrieving a single task (GET request), updating a task (PUT request), and
#    deleting a task (DELETE request). It also specifies the queryset to fetch 
#    all tasks from the database and the TaskSerializer to serialize task data.
#                                                                              
#  Additionally, this code imports the Task model and TaskSerializer from the   
#  current app's models and serializers modules, respectively. It also imports 
#  render from django.shortcuts for rendering HTML templates (though it's not  
#  used in this code snippet). Finally, it imports generics from               
#  rest_framework, which provides the generic API views used in these views.    
#                                                                              
#  These views serve as the endpoints for interacting with tasks through the   
#  API, providing CRUD functionality and leveraging DRF for serialization and  
#  API view handling.                                                          
#                                                                              
# ________________________________________________________________________________
