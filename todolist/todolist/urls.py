from django.urls import path
from .views import TaskListCreate, TaskRetrieveUpdateDestroy

urlpatterns = [
    path('task/', TaskListCreate.as_view(), name='task-list-create'),
    path('task/<int:pk>/', TaskRetrieveUpdateDestroy.as_view(), name='task-retrieve-update-destroy'),
]

# ________________________________________________________________________________
#                                                                              
#  These urlpatterns define the URL patterns for the 'todolist' app's tasks    
#  API endpoints.                                                              
#                                                                              
#  - The first path() function maps the '/task/' endpoint to the TaskListCreate
#    view, which handles listing and creating tasks. It associates the endpoint 
#    with the name 'task-list-create'.                                         
#                                                                              
#  - The second path() function maps the '/task/<int:pk>/' endpoint to the     
#    TaskRetrieveUpdateDestroy view, which handles retrieving, updating, and    
#    deleting individual tasks. It uses the primary key (pk) of the task as a  
#    URL parameter. It associates the endpoint with the name                    
#    'task-retrieve-update-destroy'.                                           
#                                                                              
#  These URL patterns define the routes that the client can use to interact    
#  with the task API endpoints.                                                
#                                                                              
# ________________________________________________________________________________
