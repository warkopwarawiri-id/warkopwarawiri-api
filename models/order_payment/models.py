from django.db import models
from enums.payment_method import PaymentMethod
from enums.payment_status import PaymentStatus

from models.order.models import Order


# Create your models here.
class OrderPayment(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    order = models.ForeignKey(
        Order,
        on_delete=models.DO_NOTHING,
    )
    status = models.PositiveSmallIntegerField(
        choices=PaymentStatus.choices(), default=PaymentStatus.WAITING.value
    )
    method = models.CharField(
        max_length=30, choices=PaymentMethod.choices(), default=PaymentMethod.CASH.value
    )
    amount = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "order_payments"
