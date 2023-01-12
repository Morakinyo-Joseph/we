from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path('', views.landing_page, name="landing_page"),

    path("login", views.log_in, name="login"),

    path("logout", views.log_out, name="logout")
]
