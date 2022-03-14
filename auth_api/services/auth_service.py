
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status

def authenticate_user(validated_data):
    user = authenticate(username=validated_data['username'], password=validated_data['password'])
    
    if user is None or not user.is_active:
        raise Exception(str(status.HTTP_401_UNAUTHORIZED))
    
    return user
    