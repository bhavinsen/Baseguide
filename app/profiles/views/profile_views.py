from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from ..models.profile import Profile
from . import api_views
import json
# Create your views here.
from rest_framework.request import Request
import requests
import json

@login_required
def create_profile(request: Request):
    """
    url_pattern: 
        /profile/create-profile/
    This view is for creating new proifle for user.
    """
    if request.method == "POST":
        if request.user.is_authenticated:
            owner_id = request.user.id
            print('owner_id: ', owner_id)

        if request.POST.get('is_verified') == 'on':
            is_verified = True
        else:
            is_verified = False
    
        data = {
            "owner_id": str(owner_id),
            "bio": request.POST.get('bio'),
            "location": request.POST.get('location'),
            "is_verified": is_verified,
            "date_of_birth": request.POST.get('date_of_birth'),
            "gender": int(request.POST.get('gender')),
            "type": int(request.POST.get('type')),
            "name": request.POST.get('name'),
            "phone_number": request.POST.get('phone_number'),
            "profile_photo": request.POST.get('profile_photo')
        }

        api_url = 'http://127.0.0.1:8000/profile/api/create-profile/'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic YWRtaW4xOmFkbWluMQ==',  # Replace with your actual authorization header
        }
        response = requests.post(api_url, headers=headers, data=json.dumps(data))

        if response.status_code == 201:
            print("Profile saved successfully!")
        else:
            print("Error saving the profile. Status code:", response.status_code)
            print("Response:", response.text)

    return render(request, "profiles/create_profile.html")

def details_profile(request, pk):
    """
    url_pattern"
        /profile/profile-details/<int:pk>/
    This view is for showing a profile's details information. 
    """
    return render(request, "profiles/details_profile.html")


def update_profile(request, pk):
    """
    url_pattern:
        /profile/profile-update/<int:pk>/
    This view is for updating a profile's information.
    """
    return render(request, "profiles/update_profile.html")


def delete_profile(request, pk):
    """
    url_pattern:
        /profile/profile-delete/<int:pk>/
    This view is for deleting a profile.
    """
    return HttpResponse("delete")
