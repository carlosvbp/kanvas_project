from django.urls import path
from accounts.views import CreateAccountView
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path("accounts/", CreateAccountView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
]
