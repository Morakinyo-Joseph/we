from django import forms
from .models import Institution, Store, Product
from account.models import User


class InstitutionCreationForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = (
            "name",
            "address",
            "institution_manager",
        )
        labels = {
            "name": "Name of Insititution"
        }


class StoreCreationForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = (
            "name",
            "owner",
            "cover_art",
            "description",
        )


class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            "product_name",
            "product_price",
            "product_category",
            "product_quantity",
            "product_description",
        )


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {
            "first_name",
            "last_name",
            "email",
        }
