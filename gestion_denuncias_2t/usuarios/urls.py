from django.urls import path
from .views import registro, login, logoutUser

urlpatterns = [
    path("registro/", registro, name='registro'),
    path("login/", login, name='login'),
    path("logout/", logoutUser, name='logout'),
]