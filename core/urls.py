from django.conf.urls import include, url

COMMON_APP_URLS = [
    url(r"^auth", include("apps.common.auth.urls", namespace="authentication"))
]

CUSTOMER_APP_URLS = []

ADMIN_APP_URLS = []

STAFF_APP_URLS = []

urlpatterns = [
    url(r"^common/", include(COMMON_APP_URLS)),
    url(r"^v1/", include(CUSTOMER_APP_URLS)),
    url(r"^admin/", include(ADMIN_APP_URLS)),
    url(r"^staff/", include(STAFF_APP_URLS)),
]
