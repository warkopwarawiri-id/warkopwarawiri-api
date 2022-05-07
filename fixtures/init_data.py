from models.account.models import Account

from .data.accounts import INIT_DATA as accounts


def init_data():
    # init anonym guest
    for account in accounts:
        if not Account.objects.filter(id=account.id).exists():
            account.save()
            print(f"-> {account.first_name} saved!")

    print("init data complete.")
