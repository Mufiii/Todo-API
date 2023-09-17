from django.shortcuts import render
from.models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class UserRegistration(APIView):
    def post(self,request):
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            user = User.objects.create_user(
                email = serializers.validated_data['email'],
                username = serializers.validated_data['username'],
                password = serializers.validated_data['password'],
                password2 = serializers.validated_data['password2']
            )
            return Response({'msg':"User Registered Successfully"}, status= status.HTTP_201_CREATED)
        return Response({"msg":serializers.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    
    
class UserView(APIView):
    def get(self,request,pk=None):
        
        user = User.objects.get(pk=request.user.id)
        print(user.id)
        serializers = UserProfileSerializer(user)
        return Response(serializers.data)
    
    def patch(self,request):
        serializers = UserProfileSerializer(request.user, data=request.data , partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response({"msg":serializers.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self,request):
        user = User.objects.get(id=request.user.id)
        user.delete()
        return Response({"msg":"Deleted Successfully"}, status=status.HTTP_200_OK)