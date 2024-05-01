from django.db import models
from profiles.models.profile import Profile
from .abstract import AbstractSocialMedia
# Create your models here.

class Artist(AbstractSocialMedia):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    artist_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.artist_name 