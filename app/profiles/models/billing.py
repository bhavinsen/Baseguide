from django.db import models 

from core.models.base import TimeStampedMixin
# Create your models here.

class BillingAddress(TimeStampedMixin):
    """
    This model represents a billing address.
    Fields:
        profile (OneToOneField): The profile associated with the billing address.
        address_line_1 (CharField): The first line of the address (required).
        address_line_2 (CharField): The second line of the address (optional).
    """
    profile = models.OneToOneField("profiles.Profile", on_delete=models.CASCADE, related_name="billing_address")
    address_line_1 = models.CharField(max_length=200)
    address_line_2 = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=100, blank=False)
    state = models.CharField(max_length=100, blank=False)
    country = models.CharField(max_length=100, blank=False)
    postal_code = models.CharField(max_length=10, blank=False)

    def __str__(self):
        return f"Billing address for {self.profile.name}"

    class Meta:
        verbose_name = "Billing Address"
        verbose_name_plural = "Billing Addresses"


class PaymentInfo(TimeStampedMixin):
    """
    This models represent a payment information.
    A payment information is associated with a specific user profile and provider.
    Fields:
        provider : Provider will be payment's method like paypal, strive etc.
    """
    profile_id = models.ForeignKey("profiles.Profile", on_delete=models.CASCADE, related_name="payment_info")
    provider = models.CharField(max_length=128)
    option_id = models.ForeignKey("profiles.ProfileOptions", on_delete=models.CASCADE)
    token_name = models.CharField(max_length=128)
    token_value = models.CharField(max_length=500)

    class Meta:
        verbose_name = "Payment Information"
        verbose_name_plural = "Payment Information"
    
