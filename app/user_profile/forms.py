from django import forms
from django.contrib.auth.models import User
from authentication.models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from profiles.models.profile import Profile
from .models.artist import Artist
from .models.partner import Partner

class CreateUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, label='First Name', widget=forms.TextInput(attrs={'placeholder':'First Name','class':'form-control'}))
    last_name=forms.CharField(max_length=100, label='Last Name', widget=forms.TextInput(attrs={'placeholder':'Last Name','class':'form-control'}))
    username=forms.CharField(max_length=100, label='Username', widget=forms.TextInput(attrs={'placeholder':'Username','class':'form-control'}))
    email=forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'placeholder':'Email','class':'form-control'}))
    class Meta:
        model = CustomUser
        fields = ["first_name","last_name","username", "email"]


class CreateProfile(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = "__all__"

class CreateArtist(forms.ModelForm):
    instagram_profile = forms.URLField(label='Instagram Profile', widget=forms.URLInput(attrs={'placeholder':'Instagram Profile','class':'form-control'}))
    apple_music_profile = forms.URLField(label='Apple Music Profile', widget=forms.URLInput(attrs={'placeholder':'Apple Music Profile','class':'form-control'})) 
    tidal_profile = forms.URLField(label='Tidal Profile', widget=forms.URLInput(attrs={'placeholder':'Tidal Profile','class':'form-control'})) 
    tiktok_profile = forms.URLField(label='Tiktok Profile', widget=forms.URLInput(attrs={'placeholder':'Tiktok Profile','class':'form-control'}))
    spotify_link = forms.URLField(label='Spotify Link', widget=forms.URLInput(attrs={'placeholder':'Spotify Link','class':'form-control'}))
    website_link = forms.URLField(label='Website Link', widget=forms.URLInput(attrs={'placeholder':'Website Link','class':'form-control'})) 
    artist_name = forms.CharField(label='Artist Name', widget=forms.TextInput(attrs={'placeholder':'Artist Name','class':'form-control'})) 
    phone_number = forms.CharField(label='Phone Number', widget=forms.TextInput(attrs={'placeholder':'Phone Number','class':'form-control'})) 

    class Meta:
        model = Artist
        exclude = ["profile",]

class CreatePartner(forms.ModelForm):

    class Meta:
        model = Partner 
        exclude = ["profile",]
        # fields = "__all__"