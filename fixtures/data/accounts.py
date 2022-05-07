import email

from enums.account_role import AccountRole
from models.account.models import Account

INIT_DATA = [
    Account(
        id=Account.ANONYM_GUEST,
        uid="NaN",
        email="NaN",
        role=AccountRole.GUEST.value,
        first_name="ANONYM",
        last_name="GUEST",
        is_verified=True,
        is_active=True,
    )
]
