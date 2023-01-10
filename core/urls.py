from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('', views.landing_page, name="landing_page"),

    path('partner', views.partnership, name="partner"),

    path('partner-create', views.create_partnership, name="partner-create"),

    path('institution-detail/<str:name>', views.institution, name="institution"),

    path('institution-detail/<str:name>/terminate', views.terminate_partnership, name="terminate-partnership"),

    path('store-create/<str:name>', views.create_store, name="store-create"),

    path("store-detail/<str:name>", views.store_detail, name="store"),

    path("product-create/<str:store_name>", views.create_product, name="product-create"),

]
