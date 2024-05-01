from django.db import models

from core.models.base import TimeStampedMixin
from profiles.models.profile import Profile
# Create your models here.

class IdentityDocument(TimeStampedMixin):
    """
    This model represents an identity document.
    An indentity document is associated with a specific user profile.
    """
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="identity_document")
    first_name = models.CharField(max_length=128, blank=False)
    middle_name = models.CharField(max_length=128, blank=True, null=True)
    last_name = models.CharField(max_length=128, blank=False)
    document_type = models.CharField(max_length=128, blank=False)
    number_document = models.CharField(max_length=128, blank=True, null=True)
    expiration_date = models.DateField( blank=False)
    issue_date = models.DateField(blank=False)
    url = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return f"Identity Document for {self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Identity Document"
        verbose_name_plural = "Identity Documents"