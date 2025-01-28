from django.urls import path
from .views import DataView


app_name = "api"

urlpatterns = [
    path("data/", DataView.as_view(), name="data")
]