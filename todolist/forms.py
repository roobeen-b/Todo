from django import forms
from django.forms import ModelForm
from .models import *

class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = "__all__"

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Enter Task...",
            }
        ),
   
    )