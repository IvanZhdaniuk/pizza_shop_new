from django import forms
from pizzashop_app.models import Order, Pizza

class OrderForm(forms.ModelForm):
    pizza = forms.ModelChoiceField(queryset=Pizza.objects.all(), widget=forms.HiddenInput)
    class Meta:
        model = Order
        fields = ('pizza', 'name', 'phone')