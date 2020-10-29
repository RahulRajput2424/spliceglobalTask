import datetime
from django.shortcuts import render
from rest_framework import  generics
from django.template import loader
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from spiceApp.models import User
from spiceApp.serializers import UserSignupSerializer, UserLoginSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import  login
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from django.http import HttpResponse

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
        profile_temp = loader.get_template('profile_temp.html')
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            token= Token.objects.get_or_create(user=user)
            response = {"data": {"message":"You have logged in successfully.",
													  "token": str(token), 
										},
								"status": 200,}
            user = User.objects.get(id = request.user.id)
            context = {"name":user.username,"type":user.get_user_type_display()}
            profile_response = profile_temp.render(context)
            profile_response = profile_temp.render(context)
            return HttpResponse(profile_response)

        else:
            error_data = serializer.errors
            return Response(data=error_data)