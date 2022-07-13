from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import *

from webtaller.models import Contacto

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

class ContactoForm(ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'

class AtencionForm(ModelForm):
    class Meta:
        model = Atencion
        fields = ['id','tipoate','descripcion','imagen','categoria','usuario']
