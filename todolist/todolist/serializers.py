from rest_framework import serializers
from .models import task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = '__all__'

# ________________________________________________________________________________
#                                                                              
#  This Django REST Framework (DRF) Serializer class, TaskSerializer,          
#  defines how the Task model data should be serialized/deserialized when      
#  interacting with the API.                                                   
#                                                                              
#  It inherits from the ModelSerializer class provided by DRF, which           
#  automatically generates serializer fields based on the Task model's fields. 
#                                                                              
#  Inside the Meta class:                                                     
#   - The model attribute specifies the model to be serialized, which is the   
#     Task model.                                                              
#   - The fields attribute is set to '__all__', indicating that all fields of  
#     the Task model should be included in the serializer.                     
#                                                                              
#  This serializer simplifies the process of serializing and deserializing     
#  Task model instances when interacting with the API endpoints.               
#                                                                              
# ________________________________________________________________________________
