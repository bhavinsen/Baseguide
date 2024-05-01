from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from authentication.models import CustomUser
from user_profile.models.artist import Artist
from profiles.models.profile import Profile
from user_profile.forms import CreateUserForm, CreateProfile, CreateArtist
# Create your views here.


@login_required
def create_artist(request):
    return HttpResponse("artist") 


@login_required
def artist_list(request):
    artists = Artist.objects.all()  
    context = {
        "artists":artists,
    }
    return render(request, "artist/artist_list.html", context)


@login_required
def artist_details(request, pk):
    artist = Artist.objects.get(pk=pk)
    context = {
        "artist": artist
    }
    return render(request, "artist/artist_details.html", context)


@login_required
def update_artist(request, pk, user_pk):
    artist = Artist.objects.get(pk=pk)
    user = CustomUser.objects.get(id=user_pk)
    profile = Profile.objects.get(owner_id=user)
    artist_form = CreateArtist(request.POST or None, instance = artist)
    profile_form = CreateProfile(request.POST or None, instance=profile)
    user_form= CreateUserForm(request.POST or None, instance=user)

    if user_form.is_valid():
        user_form.save()
        if profile_form.is_valid():
            profile_form.save()
            if artist_form.is_valid():
                artist_form.save()
                messages.success(request, "Profile has been updated")
                return HttpResponseRedirect(request.path_info)
            
    context = {
        "artist_form": artist_form,
        "user_form":user_form,
        "profile_form":profile_form
    }
    return render(request, "artist/artist_update.html", context) 


def delete_artist(request, pk):
    user = CustomUser.objects.get(pk=pk)
    user.delete()
    return HttpResponseRedirect("/profile1/artist-list/") 