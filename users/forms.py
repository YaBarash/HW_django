from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from catalog.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "password1", "password2")

    def clean_password2(self):
        cleaned_data = self.cleaned_data
        if cleaned_data['password1'] != cleaned_data['password2']:
            raise ValidationError('Пароли не совпадают!')
        return cleaned_data['password2']
