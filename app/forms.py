

from django import forms
from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['id','name', 'group','barcode','price']

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['product','quantity','group','price']


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['purchase_code', 'name','quantity','price_buy','vendor']


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['sale_code', 'product_list','total_sale','total_items','cash','change']
        
        
class PosForm(forms.ModelForm):
    class Meta:
        model = Pos
        fields = '__all__'