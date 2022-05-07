from django.db import models
from enums.category_type import CategoryType
from enums.product_categories import ProductCategories
from utils.model_manager import ModelManager
from utils.slug_generator import slug_generator

from models.business.models import Business
from models.file.models import File


# Create your models here.
class Product(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    category = models.CharField(max_length=30, choices=ProductCategories.choices())
    product_type = models.CharField(
        max_length=50, choices=CategoryType.choices(), db_column="type"
    )
    business = models.ForeignKey(to=Business, on_delete=models.DO_NOTHING)
    slug = models.SlugField(blank=True, null=True, default=None, db_index=True)
    short_name = models.CharField(max_length=20, null=True, blank=True, default=None)
    long_name = models.CharField(max_length=100, null=False, blank=False)
    price = models.PositiveIntegerField(default=0)
    picture = models.ForeignKey(
        to=File, on_delete=models.SET_DEFAULT, default=None, blank=True, null=True
    )
    description = models.TextField(max_length=3000)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)

    objects = ModelManager()
    default_objects = models.Manager()

    class Meta:
        managed = True
        db_table = "products"

    def save(self, *args, **kwargs):
        if not self.short_name:
            self.slug = slug_generator(model=Product, source=self.long_name)
        else:
            self.slug = slug_generator(model=Product, source=self.short_name)

        super(Product, self).save(*args, **kwargs)
