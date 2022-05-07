import django
from django.urls import path

from .views import AuthView

app_name = "authentication"

urlpatterns = [
    path("", AuthView.main),
]
