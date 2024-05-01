from django.conf import settings
from django.db import models
from core.models.base import TimeStampedMixin

from profiles.models.profile_option import ProfileOptions
from profiles.models.billing import BillingAddress


GENDER_CHOICES = (
    (1, "Male"),
    (2, "Female"),
    (3, "Other"),
)

PROFILE_TYPE_CHOICES = (
    (1, "Person"),
    (2, "Company"),
)

class Profile(TimeStampedMixin):
    """
    A profile model that stores information about a user after subscribe.

    Fields:
        owner_id: The ID of the user who owns the profile.
        type: The type of profile.
        name: Name will come from identity document.For a person,
              person's first name and last name from identity documents will be
              profile's name. For company, company name from identity documents
              will be profile's name.
    """
    owner_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(max_length=1000, blank=True, null=True)
    location = models.CharField(max_length=128, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.IntegerField(choices=GENDER_CHOICES, blank=True, null=True)
    profile_photo = models.ImageField(
        blank=True,
        null=True,
        upload_to="profile_photos/",
    )
    type = models.IntegerField( choices=PROFILE_TYPE_CHOICES, default=1,blank=False)
    name = models.CharField(max_length=128, blank=False)
    phone_number = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
       
    def get_billing_address(self):
        billing_address = BillingAddress.objects.filter(profile=self).first()
        if billing_address is None:
            billing_address = BillingAddress.objects.create(profile=self, address_line_1="profile address")
        return billing_address
        
    def set_billing_address(self, address_data):
        billing_address = self.get_billing_address()
        if billing_address:
            billing_address.address_line_1 = address_data.get('address_line_1', billing_address.address_line_1)
            billing_address.address_line_2 = address_data.get('address_line_2', billing_address.address_line_2)
            billing_address.city = address_data.get('city', billing_address.city)
            billing_address.state = address_data.get('state', billing_address.state)
            billing_address.country = address_data.get('country', billing_address.country)
            billing_address.postal_code = address_data.get('postal_code', billing_address.postal_code)
            billing_address.save()
            return True
        return False


class Role(TimeStampedMixin):
    """
    This model reperents user role.
    """
    name = models.CharField(max_length=128, blank=False)

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"


class ProfileRole(TimeStampedMixin):
    """
    This model represents role of company/ project.
    """
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{ self.profile_id} ({self.role_id})"
    
    class Meta:
        verbose_name = "Profile Role"
        verbose_name_plural = "k"


class ProfileInfo(TimeStampedMixin):
    """
    A profile info model that stores information about a profile.
    """
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    type = models.IntegerField(blank=False)
    option_id = models.ForeignKey(ProfileOptions, on_delete=models.CASCADE)
    value = models.CharField(max_length=128, blank=False)

    def __str__(self):
        return f"{self.profile_id} ({self.type})"

    class Meta:
        verbose_name = "Profile Information"
        verbose_name_plural = "Profile Information"


class ProfileUser(TimeStampedMixin):
    """
    A profile user model that stores information about a user who is assigned to a role.
    """
    profile_id = models.ForeignKey(ProfileRole, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.profile_id} ({self.user_id})"
    
    class Meta:
        verbose_name = "Profile User"
        verbose_name_plural = "Profile Users"
        
class ContactDetails(models.Model):
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=12, blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    IM = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return f"{self.profile_id} ({self.name})"
