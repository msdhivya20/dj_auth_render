from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):

    email=forms.EmailField()

    def __init__(self,*args,**kwargs):

        super().__init__(*args,**kwargs)

        for field in self.fields.values():

            field.widget.attrs[
                'class'
            ]='form-control'

    class Meta:

        model=User

        fields=[
            'username',
            'email',
            'password1',
            'password2'
        ]

    def clean_username(self):

        username=self.cleaned_data['username']

        if User.objects.filter(
            username=username
        ).exists():

            raise forms.ValidationError(
                "Username already exists"
            )

        return username

    def clean_email(self):

        email=self.cleaned_data['email']

        if User.objects.filter(
            email__iexact=email
        ).exists():

            raise forms.ValidationError(
                "Email already registered"
            )

        return email