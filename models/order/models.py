from django.db import models
from enums.order_status import OrderStatus

from models.account.models import Account


# Create your models here.
class Order(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    number = models.CharField(max_length=30, null=True, blank=True, default=None)
    current_status = models.PositiveSmallIntegerField(
        choices=OrderStatus.choices(), default=OrderStatus.UNCONFIRMED.value
    )
    total_price = models.PositiveBigIntegerField(default=0)
    is_anonym = models.BooleanField(default=False)
    guest_info = models.JSONField()
    guest = models.ForeignKey(
        Account, on_delete=models.SET_DEFAULT, default=Account.ANONYM_GUEST
    )
    note = models.TextField(null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        managed = True
        db_table = "orders"
