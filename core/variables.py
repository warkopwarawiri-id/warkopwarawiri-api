from pathlib import Path

DEBUG = True

d = "models"
APPLICATIONS = [
    f"{d}.account.apps.AccountConfig",
    f"{d}.business.apps.BusinessConfig",
    f"{d}.order.apps.OrderConfig",
    f"{d}.order_item.apps.OrderItemConfig",
    f"{d}.order_payment.apps.OrderPaymentConfig",
    f"{d}.product.apps.ProductConfig",
    f"{d}.socmed.apps.SocmedConfig",
    f"{d}.contact.apps.ContactConfig",
    f"{d}.file.apps.FileConfig",
    f"{d}.order_status.apps.OrderStatusConfig",
    f"{d}.authenticated_account.apps.AuthenticatedAccountConfig",
]

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

ALLOWED_ORIGINS = ["http://localhost", "http://127.0.0.1"]

ALLOWED_HEADERS = ["Authorization", "X-Requested-With", "Content-Type"]

SECRET_KEY = "=a9o+ie37=f^j=^r5k4^ec95ia#so#8rb(!o(&*%*+)6d=j@o*"

BASE_DIR = Path(__file__).resolve().parent.parent

DB_CONFIG = {
    "mysql": {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": "www_local",
            "USER": "root",
            "PASSWORD": "root",
            "HOST": "localhost",
            "PORT": "3306",
        }
    },
    "sqlite": {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    },
}

app_config = {
    "applications": APPLICATIONS,
    "secret_key": SECRET_KEY,
    "is_debug": DEBUG,
    "allowed_host": ALLOWED_HOSTS,
    "database": DB_CONFIG.get("mysql"),
    "base_dir": BASE_DIR,
    "allowed_origins": ALLOWED_ORIGINS,
    "allowed_headers": ALLOWED_HEADERS,
}
