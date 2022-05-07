import uuid

from django.db import models
from enums.file_type import FileType


# Create your models here.
class File(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    file_type = models.CharField(
        max_length=50, choices=FileType.choices(), db_column="type"
    )
    name = models.CharField(max_length=100, null=False, blank=False)
    ext = models.CharField(max_length=10, null=False, blank=False)
    location = models.CharField(max_length=256, null=True, blank=True, default=None)
    url = models.CharField(max_length=256, null=False, blank=False)

    class Meta:
        managed = True
        db_table = "files"
