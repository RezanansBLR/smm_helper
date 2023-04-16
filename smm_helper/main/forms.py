from django import forms
from .models import *

class Search(forms.Form):
    url = forms.CharField(max_length=255, label='', widget=forms.TextInput(attrs={'class':'form-input'}))