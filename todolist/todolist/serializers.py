from rest_framework import serializers
from .models import task

class TaskSerializer(serializers.ModelSerializer):
    class meta:
        model = task
        fields = '__all__'