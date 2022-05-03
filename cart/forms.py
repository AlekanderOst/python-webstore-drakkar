from .models import Cart
from django.forms import ModelForm, TextInput


class CartForm(ModelForm):

    class Meta:
        model = Cart
        fields = ['cost','choose_color','img']
        exclude = ['img']
        widgets = {
            "cost": TextInput(attrs={'type': 'hidden'}),
        }





