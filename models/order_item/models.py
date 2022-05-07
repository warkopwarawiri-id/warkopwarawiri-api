from django.db import models

from models.order.models import Order
from models.product.models import Product


# Create your models here.
class OrderItem(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    order = models.ForeignKey(
        Order,
        on_delete=models.DO_NOTHING,
    )
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    qty = models.PositiveSmallIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    note = models.TextField()

    class Meta:
        managed = True
        db_table = "order_items"
