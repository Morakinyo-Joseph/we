from django.urls import path
from . import views

app_name = "supermarket"

urlpatterns = [
    path("home", views.homepage, name="homepage")
]
