DEBUG = True

d = 'models'
APPLICATIONS = [
    f'{d}.account.apps.AccountConfig',
    f'{d}.business.apps.BusinessConfig',
    f'{d}.order.apps.OrderConfig',
    f'{d}.order_item.apps.OrderItemConfig',
    f'{d}.order_payment.apps.OrderPaymentConfig',
    f'{d}.product.apps.ProductConfig'
]

ALLOWED_HOSTS = []

SECRET_KEY = '=a9o+ie37=f^j=^r5k4^ec95ia#so#8rb(!o(&*%*+)6d=j@o*'

app_config = {
    'applications': APPLICATIONS,
    'secret_key': SECRET_KEY,
    'is_debug': DEBUG,
    'allowed_host': ALLOWED_HOSTS
}