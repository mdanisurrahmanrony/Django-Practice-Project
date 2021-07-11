from django import forms
from django.core import validators
from django_practice_app import models

class MusicianForm(forms.ModelForm):
      class Meta:
          model = models.Musician
          fields = "__all__"
