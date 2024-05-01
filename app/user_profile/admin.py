from django.contrib import admin
from user_profile.models import artist, partner
from profiles.models.profile import Profile
# Register your models here.

admin.site.register(artist.Artist)
admin.site.register(partner.Partner)
admin.site.register(Profile)