from django.apps import AppConfig


class TodolistConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todolist'

# ______________________________________________________________________________
#                                                                              
#  This Django AppConfig class, TodolistConfig, is responsible for configuring 
#  the 'todolist' app within the Django project.                               
#                                                                              
#  It specifies the default_auto_field as 'django.db.models.BigAutoField',      
#  indicating the default primary key type for models in the app. This field   
#  type is used for automatic primary key generation with a larger range.      
#                                                                              
#  The name attribute specifies the name of the app, which is 'todolist'.      
#                                                                              
# ______________________________________________________________________________
