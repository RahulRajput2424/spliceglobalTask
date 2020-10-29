import datetime
from django.shortcuts import render
from rest_framework import  generics
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from spiceApp.models import User
from spiceApp.serializers import UserSignupSerializer, UserLoginSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import  login
from rest_framework import status
class UserSignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignupSerializer
    authentication_classes = []
    permission_classes = []

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'status': 200,
            'message': 'Successfully Created, Please Sign-In`',
            'data': response.data
        })

class UserLoginView(APIView):
    authentication_classes = []
    permission_classes = []
    
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            token= Token.objects.get_or_create(user=user)
            response = {"data": {"message":"You have logged in successfully.",
													  "token": str(token), 
										},
								"status": 200,}
            return Response(response, status=status.HTTP_200_OK)
        else:
            error_data = serializer.errors
            return Response(data=error_data)