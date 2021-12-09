from django import forms
from .models import Product

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'product_name',
            'slug',
            'description',
            'price',
            'images',
            'stock',
            'is_available',
            'category',
        ]