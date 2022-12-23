from .models import Usuario
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

class RegistroUsuarioForm(UserCreationForm):

    class Meta:
        model  = Usuario
        fields = ['first_name','last_name','username','password1','password2','email', 'imagen']

