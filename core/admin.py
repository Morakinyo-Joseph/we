from django.contrib import admin
from .models import Cart, Category, Institution, Product, Store

# Register your models here.


admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(Institution)
admin.site.register(Product)
admin.site.register(Store)

