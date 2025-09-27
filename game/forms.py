from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
import re

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username',)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 5:
            raise forms.ValidationError("Username must be at least 5 characters long.")
        if not (any(c.islower() for c in username) and any(c.isupper() for c in username)):
            raise forms.ValidationError("Username must contain both uppercase and lowercase letters.")
        return username

    def clean_password2(self):
        password = self.cleaned_data.get("password2")
        if len(password) < 5:
            raise forms.ValidationError("Password must be at least 5 characters long.")
        if not re.search(r'[A-Za-z]', password):
            raise forms.ValidationError("Password must contain at least one letter.")
        if not re.search(r'\d', password):
            raise forms.ValidationError("Password must contain at least one number.")
        if not re.search(r'[$%*@]', password):
            raise forms.ValidationError("Password must contain one of the following: $, %, *, @.")
        return password

class GuessForm(forms.Form):
    guess = forms.CharField(
        label='',
        max_length=5,
        min_length=5,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'w-full max-w-xs p-3 text-2xl text-center font-mono tracking-widest uppercase border-2 border-gray-400 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500',
            'placeholder': 'GUESS',
            'autofocus': True
        })
    )

    def clean_guess(self):
        guess = self.cleaned_data.get('guess', '').upper()
        if not guess.isalpha() or len(guess) != 5:
            raise forms.ValidationError("Please enter a valid 5-letter word.")
        return guess