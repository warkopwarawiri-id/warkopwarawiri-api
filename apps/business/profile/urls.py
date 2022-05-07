from django.urls import path

from .views import PtofileViews as views

app_name = "business_profile"

urlpatterns = [
    path("<slug:slug>", views.main),
]
