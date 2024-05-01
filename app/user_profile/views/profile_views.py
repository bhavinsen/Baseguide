from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect 
from django.contrib import messages
from user_profile.forms import CreateUserForm, CreateProfile, CreateArtist
# Create your views here.

@login_required
def create_profile(request):
    if request.method == "POST":
        user_form = CreateUserForm(request.POST)
        artist_form=CreateArtist(request.POST)
        profile_form=CreateProfile(request.POST)
        if user_form.is_valid() and profile_form.is_valid() and artist_form.is_valid():
            user = user_form.save()
            profile_form.save(commit=False)
            profile_form.instance.owner_id = user.id
            profile_form.instance.user = user
            profile=profile_form.save()
            artist_form.save(commit=False)
            artist_form.instance.profile = profile
            artist_form.save()
            messages.success(request,"Your account has been created")
            return HttpResponseRedirect("/profile1/artist-list/")
    profile_form=CreateProfile()
    artist_form = CreateArtist()
    user_form = CreateUserForm()
    context = {
        "profile_form":profile_form,
        "user_form":user_form,
        "artist_form":artist_form,
    }
    return render(request, "create_profile.html", context) 

