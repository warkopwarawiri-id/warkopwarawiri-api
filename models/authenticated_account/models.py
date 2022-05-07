from django.db import models

from models.account.models import Account


# Create your models here.
class AuthenticatedAccount(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    auth_token = models.CharField(max_length=256, null=True, blank=True, default=None)
    fcm_token = models.CharField(max_length=256, null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "authenticated_accounts"
