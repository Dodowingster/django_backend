from django.contrib import admin
from .models import task

# Register your models here.
admin.site.register(task)

# ________________________________________________________________________________
#                                                                              
#  This code registers the Task model with the Django admin interface.         
#                                                                              
#  - It imports the admin module from django.contrib and the Task model from    
#    the current app's models module.                                          
#                                                                              
#  - Then, it calls the register() method of the admin.site object, passing    
#    the Task model as an argument. This tells Django to make the Task model   
#    accessible via the admin interface.                                       
#                                                                              
#  By registering the Task model, administrators can manage tasks directly    
#  through the Django admin interface, including creating, editing, and       
#  deleting tasks.                                                             
#                                                                              
# ________________________________________________________________________________
