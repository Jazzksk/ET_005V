from django import forms
from django.db.models import fields
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

""" 
    PRODUCTO 
"""
class FormProducto(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ('titulo','imagen','descripcion','stock','precio','descuento','categoria')
        """ widgets = {
            'titulo': forms.TextInput(),
            'descripcion' : forms.Textarea(),
            'stock' : forms.NumberInput(),
            'precio' : forms.NumberInput(),
            'descuento' : forms.NumberInput(),
            'imagen' : forms.FileField()
        } """
        """ widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ingrese el nombre del producto...' , 'required': True}),
            'descripcion' : forms.Textarea(attrs={'class' : 'form-control', 'row' : 3, 'required': True}),
            'stock' : forms.NumberInput(attrs={'class' : 'form-control', 'placeholder':'XXXX', 'required': True}),
            'precio' : forms.NumberInput(attrs={'class' : 'form-control', 'placeholder':'XXXX.XX', 'required': True}),
            'descuento' : forms.NumberInput(attrs={'class' : 'form-control', 'placeholder':'XX%', 'required': True}),
            'imagen' : forms.FileField(attrs={'class':'form-control-file', 'id':'imagen', 'placeholder': 'Ingrese la imagen...', 'required': True})
        } """

