from django.db import models

from core.models.base import TimeStampedMixin
from profiles.models.billing import PaymentInfo
# Create your models here.

class ProfileOptions(TimeStampedMixin):
    """
    This model represents a profile option.
    The profile option is associated with a specific use profile.
    Fields:
        type_payment : Type of option.
    """
    PROFILE_TYPE = ((1, "Individual"),(2, "Company"),)
    type = models.IntegerField(choices=PROFILE_TYPE, blank=False)
    name = models.CharField(max_length=128, blank=False)
    value = models.CharField(max_length=128,blank=False)
    icon = models.CharField(max_length=128, blank=True, null=True) 

    class Meta:
        verbose_name = "Profile Option"
        verbose_name_plural = "Profile Options"

    def __str__(self):
        return f"{self.name} ({self.type})"