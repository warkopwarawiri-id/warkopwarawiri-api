from django.conf.urls import include, url

COMMON_APP_URLS = [
    url(r"^auth/", include("apps.common.auth.urls", namespace="authentication"))
]

CUSTOMER_APP_URLS = []

BUSINESS_APP_URLS = [
    url(r"^order/", include("apps.business.order.urls", namespace="business_order"))
]

urlpatterns = [
    url(r"^common/", include(COMMON_APP_URLS)),
    url(r"^v1/", include(CUSTOMER_APP_URLS)),
    url(r"^business/", include(BUSINESS_APP_URLS)),
]
