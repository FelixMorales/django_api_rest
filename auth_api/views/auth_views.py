from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework import serializers
from rest_framework.views import APIView
from django.contrib.auth import login, logout
from django.contrib.auth.models import User


import auth_api.services.auth_service

class LoginView(APIView):
    class InputSerializer(serializers.Serializer):
        username = serializers.CharField()
        password = serializers.CharField()
    
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'username')

    def post(self, request: Request):
        try:
            input = self.InputSerializer(data=request.data)
            input.is_valid(raise_exception=True)
            user = auth_api.services.auth_service.authenticate_user(input.validated_data)
            login(request=request, user=user)
            output = self.OutputSerializer(user)
            return Response(output.data)
        except Exception as error:
            return Response(str(error), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LogoutView(APIView):

    def post(self, request):
        try:
            logout(request=request)
            return Response('Logout successfully')
        except Exception as error:
            return Response(str(error), status=status.HTTP_500_INTERNAL_SERVER_ERROR)