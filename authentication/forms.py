from django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    ROLE_CHOICES = (
       ('Pelanggan', 'Pelanggan'),
        ('Karyawan', 'Karyawan'),
    )

    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        widget=forms.RadioSelect
    )
