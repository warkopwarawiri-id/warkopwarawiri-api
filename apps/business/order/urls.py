from django.urls import path

from .views import OrderViews as views

app_name = "business_order"

urlpatterns = [
    path("<slug:slug>", views.main),
]
