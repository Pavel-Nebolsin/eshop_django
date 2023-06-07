from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from useraccount.models import Profile
import re


class ProfileForm(forms.Form):
    first_name = forms.CharField(label='Имя', max_length=50, widget=forms.TextInput(attrs={'disabled': True, 'class': 'form-control'}))
    last_name = forms.CharField(label='Фамилия', max_length=50, widget=forms.TextInput(attrs={'disabled': True, 'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'disabled': True, 'class': 'form-control'}))
    phone_number = forms.CharField(label='Телефон', max_length=20, widget=forms.TextInput(attrs={'disabled': True, 'class': 'form-control', 'placeholder': 'Например +79991234567'}))
    address = forms.CharField(label='Адрес', widget=forms.Textarea(attrs={'disabled': True, 'class': 'form-control text-break address-input', 'rows': 3, 'placeholder': 'Ваш адрес для доставки'}))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        initial_email = self.initial.get('email')

        if email == str(initial_email):
            return email

        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError("Пользователь с таким email уже существует.")

        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        initial_phone_number = self.initial.get('phone_number')
        errors = []

        if phone_number == initial_phone_number:
            return phone_number

        if phone_number and Profile.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("Пользователь с таким номером уже существует.")

        if not validate_phone_number(phone_number):
            errors.append(forms.ValidationError("Неверный формат (Пример: +79991234567)"))

        if errors:
            raise forms.ValidationError(errors)

        return phone_number


def validate_phone_number(phone_number):
    pattern = r'^\+7\d{10}$'
    if re.match(pattern, phone_number):
        return True
    return False
