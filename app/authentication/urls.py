from django.urls import path

from .views import RegistrationView


app_name = "auth"

PROFILE_URLPATTERNS = [
    path('register/', RegistrationView.as_view(), name='register'),
]

urlpatterns = [
    *PROFILE_URLPATTERNS,
]

