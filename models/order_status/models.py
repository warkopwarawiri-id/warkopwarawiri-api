from django.db import models
from enums.order_status import OrderStatus as status

from models.account.models import Account
from models.order.models import Order


# Create your models here.
class OrderStatus(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    order = models.ForeignKey(
        Order,
        on_delete=models.DO_NOTHING,
    )
    before = models.PositiveSmallIntegerField(choices=status.choices())
    after = models.PositiveSmallIntegerField(choices=status.choices())
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Account, on_delete=models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = "order_status"
