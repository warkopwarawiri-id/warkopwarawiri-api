from django.db import models
from enums.contact_type import ContactType
from enums.property_owner import PropertyOwner
from utils.model_manager import ModelManager


# Create your models here.
class Contact(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    contact_type = models.CharField(
        max_length=50, choices=ContactType.choices(), db_column="type"
    )
    owner_type = models.CharField(max_length=100, choices=PropertyOwner.choices())
    owner_ref = models.BigIntegerField(editable=False)
    value = models.CharField(max_length=100, blank=False, null=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)

    objects = ModelManager()
    default_objects = models.Manager()

    class Meta:
        managed = True
        db_table = "contacts"
