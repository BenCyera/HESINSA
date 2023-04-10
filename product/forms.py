from django.contrib.auth.forms import forms
from .models import Product, Inbound


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'code', 'description', 'price', 'size', 'inventory', 'input_date', 'output_date']


class InboundForm(forms.ModelForm):
    pass


class OutboundForm(forms.ModelForm):
    pass
