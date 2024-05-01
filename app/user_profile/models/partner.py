from django.db import models
from .artist import Artist
from profiles.models.profile import Profile
from .abstract import  AbstractCompany, AbstractFinance
# Create your models here.


class Partner(AbstractCompany, AbstractFinance):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    artist = models.ManyToManyField(Artist)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
     
    def __str__(self):
        return str(self.profile)