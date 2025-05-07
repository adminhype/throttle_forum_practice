from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from user_auth_app.serializers import RegistrationSerializer
from rest_framework.permissions import AllowAny

# Create your views here.
class  RegistrationView(CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]