from django.db import models
from django.contrib.auth.models import User
from authentication.models import CustomUser
from .abstract import TimeStampedModel
from .artist import Artist
from .partner import Partner
# Create your models here.

# gender_choices =(
#     (1,'Male'),
#     (2,'Female'),
# )

# class Profile(TimeStampedModel):
#     user = models.OneToOneField(User, on_delete=models.CASCADE,  null=True, blank=True)
#     photo = models.ImageField(
#         null=True,
#         blank=True,
#         upload_to="profile_photos/"
#     )
#     gender = models.PositiveSmallIntegerField(choices=gender_choices)

#     def __str__(self):
#         return str(self.user)
    
# class Invoice(models.Model):

#     invoice_name = models.CharField(max_length=100,default='')
#     duedate = models.CharField(max_length=100,default='')
#     partnername = models.ForeignKey(Partner,on_delete=models.CASCADE,null=True)
#     artistname = models.ForeignKey(Artist,on_delete=models.CASCADE,null=True)
#     servicesname1 = models.CharField(max_length=100, default='')
#     servicesname2 = models.CharField(max_length=100, default='',blank=True,null=True)
#     amount1 = models.CharField(max_length=100, default='')
#     amount2 = models.CharField(max_length=100, default='',blank=True,null=True)
#     paid = models.BooleanField(default=False)
    
class Invoice(models.Model):
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    invoice_name = models.CharField(max_length=100, default='')
    duedate = models.CharField(max_length=100, default='')
    partnername = models.ForeignKey(Partner, on_delete=models.CASCADE, null=True)
    artistname = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)
    services = models.JSONField(default=list)  
    amounts = models.JSONField(default=list)   
    paid = models.BooleanField(default=False)
    vat = models.BooleanField(default=True)