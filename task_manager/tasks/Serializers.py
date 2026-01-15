from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'owner']
        read_only_fields = ['owner'] # مهم حتى يعين المالك تلقائيًا

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) 
    tasks = TaskSerializer(many=True, read_only=True) 
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'tasks']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'],
                                        email=validated_data['email'],
                                        password=validated_data['password'])
        return user
    

    