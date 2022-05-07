from django.db import models
from enums.property_owner import PropertyOwner
from enums.socmed_type import SocmedType
from utils.model_manager import ModelManager


# Create your models here.
class Socmed(models.Model):
    socmed_type = models.CharField(
        max_length=50, choices=SocmedType.choices(), db_column="type"
    )
    owner_type = models.CharField(max_length=100, choices=PropertyOwner.choices())
    owner_ref = models.BigIntegerField(editable=False)
    value = models.CharField(max_length=100, blank=False, null=False)
    url = models.CharField(max_length=256, blank=False, null=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)

    objects = ModelManager()
    default_objects = models.Manager()

    class Meta:
        managed = True
        db_table = "socmeds"
