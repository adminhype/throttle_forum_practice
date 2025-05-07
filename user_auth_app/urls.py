from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from user_auth_app.views import RegisterView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
]