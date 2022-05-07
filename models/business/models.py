from django.db import models
from utils.model_manager import ModelManager
from utils.slug_generator import slug_generator

from models.account.models import Account
from models.file.models import File


# Create your models here.
class Business(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    slug = models.SlugField(blank=True, null=True, default=None, db_index=True)
    owner = models.ForeignKey(to=Account, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100, null=False, blank=False)
    picture = models.ForeignKey(
        to=File, on_delete=models.SET_DEFAULT, default=None, blank=True, null=True
    )
    location_lat = models.CharField(max_length=100, null=True, blank=True, default=None)
    location_lng = models.CharField(max_length=100, null=True, blank=True, default=None)
    address = models.TextField(null=False, blank=False)
    city = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    email = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)

    objects = ModelManager()
    default_objects = models.Manager()

    class Meta:
        managed = True
        db_table = "business"

    def save(self, *args, **kwargs):
        self.slug = slug_generator(model=Business, source=self.name)
        super(Business, self).save(*args, **kwargs)
