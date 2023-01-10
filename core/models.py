from django.db import models
from accounts.models import User
import uuid

# Create your models here.


class Institution(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)     
    name = models.CharField(max_length=1000)
    address = models.CharField(max_length=3000)
    institution_manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name="institution")
    date_joined = models.DateTimeField(auto_now_add=True)


class Store(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name="store")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    capacity = models.IntegerField(default=100)
    cover_art = models.ImageField()
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="product")
    product_name = models.CharField(max_length=500)
    product_id = models.CharField(max_length=20)
    product_price = models.FloatField(default=0.00)
    product_category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="product")
    product_quantity = models.IntegerField(default=1)
    product_description = models.TextField(max_length=5000)
    sold_out = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="image")
    file = models.ImageField()


class Category(models.Model):
    category = models.CharField(max_length=1000)


class Cart(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="cart")
    cart_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_cart")
    empty = models.BooleanField(default=False)