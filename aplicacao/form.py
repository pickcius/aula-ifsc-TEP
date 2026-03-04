from django.forms import fields 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreations
from django import forms

class UsuarioForm(UserCreations):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

        widgets = {

            'username': forms.TextImput(attrs={

                'class': 'form-control'

            }),
        

            'email': forms.TextImput(attrs={

                'class': 'form-control'

            }),
            
        }

