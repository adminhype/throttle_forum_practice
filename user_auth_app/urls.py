from os import path
from rest_framework.authtoken.views import obtain_auth_token
from user_auth_app.views import RegistrationView


urlpatterns = [
    path('login/', obtain_auth_token),
    path('register/', RegistrationView.as_view()),
]