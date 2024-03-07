from django import forms

from career.models import Career
from .models import Stage

class CandidateForm(forms.Form):
    first_name = forms.CharField(max_length=150)
    last_name=forms.CharField(max_length=150)
    email=forms.EmailField()
    username=forms.CharField(
        max_length=150
    )
    password=forms.CharField(
        max_length=150,
        widget=forms.PasswordInput
    )
    career=forms.ModelChoiceField(Career.objects.all())
    stage=forms.ModelChoiceField(Stage.objects.all())