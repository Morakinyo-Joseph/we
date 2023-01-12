from django.urls import path
from . import views

app_name = "core"

urlpatterns = [

    path('dashboard', views.dashboard, name="dashboard"),

    # partnership
    path('partner-create', views.create_partnership, name="partner-create"),

    # manage institution
    path('institution-detail/<str:name>', views.institution, name="institution"),
    path('institution-detail/<str:name>/terminate', views.terminate_partnership, name="terminate-partnership"),

    # manage store
    path('store-create/<str:name>', views.create_store, name="store-create"),
    path("store-detail/<str:name>", views.store_detail, name="store"),

    # manage product
    path("product-create/<str:store_name>", views.create_product, name="product-create"),

    # manage user
    path("user-list", views.user_list, name="user-list"),
    path("user-create", views.create_user, name="user-create"),
]
