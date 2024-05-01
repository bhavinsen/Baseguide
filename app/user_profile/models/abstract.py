from django.db import models
# Create your models here.

class TimeStampedModel(models.Model):
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    class Meta:
        
        abstract = True


class AbstractContact(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email_address = models.EmailField(max_length=150, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        
        abstract = True


class AbstractCompany(models.Model):
    company_name = models.CharField(max_length=100, blank=True, null=True)
    coc_number = models.CharField(max_length=30, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(max_length=25, blank=True, null=True)
    
    class Meta:
        
        abstract = True


class AbstractFinance(models.Model):
    accountholder = models.CharField(max_length=100, blank=True, null=True)
    bankaccount_number = models.CharField(max_length=100, blank=True, null=True)
    bic_code = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        
        abstract = True


class AbstractSocialMedia(models.Model):
    instagram_profile = models.URLField(max_length = 200, blank=True, null=True)
    apple_music_profile = models.URLField(max_length = 200, blank=True, null=True) 
    tidal_profile = models.URLField(max_length = 200, blank=True, null=True) 
    tiktok_profile = models.URLField(max_length = 200, blank=True, null=True)
    spotify_link = models.URLField(max_length = 200, blank=True, null=True)
    website_link = models.URLField(max_length = 200, blank=True, null=True) 

    class Meta:
        
        abstract = True
