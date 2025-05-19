from django import forms
from django.core.exceptions import ValidationError
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

    def clean_name(self):
        name = self.cleaned_data["name"]
        # Check if the name already exists for the user
        if name.startswith("X"):
            raise forms.ValidationError("No name should start with 'X'.")
        return name

    def clean_email(self):
        email = self.cleaned_data["email"]
        # Check if the email already exists for the user
        if Contact.objects.filter(user=self.initial.get("user"), email=email).exists():
            raise forms.ValidationError(
                "You already have a contact with this email address."
            )
        return email

    class Meta:
        model = Contact
        fields = ("name", "email")
