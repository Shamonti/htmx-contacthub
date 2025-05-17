from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "input input-bordered w-full", "placeholder": "Insert Name"}
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "input input-bordered w-full",
                "placeholder": "Insert Email",
            }
        )
    )

    class Meta:
        model = Contact
        fields = ("name", "email")
