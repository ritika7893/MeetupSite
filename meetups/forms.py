# forms.py
from django import forms


class RegistrationForm(forms.Form):
    name = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={"placeholder": "Your Name", "class": "form-control"}
        ),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"placeholder": "Your Email", "class": "form-control"}
        )
    )
    phone = forms.CharField(  # Changed from IntegerField
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Your Phone Number", "class": "form-control"}
        ),
    )
