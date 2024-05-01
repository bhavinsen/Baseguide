from django.db import models
from user_profile.models.artist import Artist
from authentication.models import CustomUser
from core.models.base import TimeStampedMixin

class Booking(models.Model):
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    artist_name = models.ForeignKey(Artist, blank=True, null=True, on_delete=models.DO_NOTHING )
    
    #event info
    event_name = models.CharField(max_length=100, default='', blank=True)
    event_date = models.DateField(blank=True, null=True)
    venue_name = models.CharField(max_length=100, default='', blank=True)
    start_time_performance = models.DateTimeField(blank=True, null=True)
    performance_duration_in_minutes = models.CharField(max_length=4, default='', blank=True)

    #booker info
    first_name = models.CharField(max_length=100, default='', blank=True)
    last_name = models.CharField(max_length=100, default='', blank=True)
    business_name = models.CharField(max_length=100, default='', blank=True)
    phone_number = models.CharField(max_length=100, default='', blank=True)
    email_address = models.EmailField(max_length=100, default='', blank=True)

    #Deal info
    flatfee = models.CharField(max_length=100, default='',blank=True, null=True) 
    vat_amount = models.CharField(max_length=100, default='',blank=True, null=True) 
    invoice_paid = models.BooleanField(default=False)
    
    extra_comments = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.event_name} {self.event_name}"

