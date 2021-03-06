from django.contrib.auth.models import User
from rest_framework import serializers
from todos.models import Todo


class TodoUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username", "email", "date_joined")


class TodoSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        print "create"
    def validate(self, attrs):
        print "validate"
        
    user = TodoUserSerializer(read_only=True)

    class Meta:
        model = Todo
        fields = ("user", "name", "done", "date_created")
