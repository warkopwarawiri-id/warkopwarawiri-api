from django.db import models
from enums.account_role import AccountRole
from utils.model_manager import ModelManager

from models.file.models import File


# Create your models here.
class Account(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    uid = models.CharField(max_length=50, null=False, blank=False)
    email = models.CharField(max_length=150, null=False, blank=False, unique=True)
    role = models.CharField(max_length=30, choices=AccountRole.choices())
    first_name = models.CharField(max_length=75, null=False, blank=False)
    middle_name = models.CharField(max_length=75, null=True, blank=True, default=None)
    last_name = models.CharField(max_length=75, null=True, blank=True, default=None)
    picture = models.ForeignKey(
        to=File, on_delete=models.SET_DEFAULT, default=None, blank=True, null=True
    )
    registered_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(null=False, blank=False, default=True)
    last_update = models.DateTimeField(auto_now=True, null=True, blank=True)
    is_deleted = models.BooleanField(null=False, blank=False, default=False)
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)

    objects = ModelManager()
    default_objects = models.Manager()

    ANONYM_GUEST = 1

    class Meta:
        managed = True
        db_table = "accounts"
