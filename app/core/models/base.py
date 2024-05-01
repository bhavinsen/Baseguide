from django.db import models

# Create your models here.

class TimeStampedMixin(models.Model):
    """
    A mixin that adds timestamp fields to a model.

    Fields:
        created_at: The date and time when the model was created.
        updated_at: The date and time when the model was last updated.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:

        abstract = True


class BaseModel(TimeStampedMixin):
    """
    A base model that adds timestamp fields and a verified field to a model.

    Fields:
        is_verified: Whether or not the model has been verified.
    """
    is_verified = models.BooleanField()

    class Meta:

        abstract = True                                                                                                                                                                                                                                                                                                                 