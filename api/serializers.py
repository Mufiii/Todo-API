from rest_framework import serializers
from .models import *
from rest_framework.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta :
        model = User
        fields = ('id','username','email','password','password2')
        
        
    def validate(self,data):
        password = data.get('password')
        password2 = data.get('password2')
        if password != password2 :
            raise ValidationError("Password Does not Match")
        return data
    
class UserProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    
    class Meta :
        model = User
        fields = ('id','first_name',"last_name","username","email")
    