from django import forms
from .models import Status, Order, ProductsInOrder, ProductInBasket


class CheckoutContactForm(forms.Form):
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)