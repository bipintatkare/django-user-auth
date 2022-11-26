from django.urls import path
from .views import auth, register, login


urlpatterns = [
    path('auth/', auth, name="auth"),
    path('register/', register, name="register"),
    path('login/', login, name="login"),
]