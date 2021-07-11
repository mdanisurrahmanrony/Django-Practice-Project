from django import forms
from django.core import validators

def even_or_not(value):
    if value%2 == 1:
        raise forms.ValidationError("Please Insert an Even Number!")

class user_form(forms.Form):
    number_field = forms.IntegerField(validators=[even_or_not])
