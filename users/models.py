from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    phone_number = PhoneNumberField(blank=True, region='RU', verbose_name='номер телефона', null=True,
                                    help_text='Введите номер телефона')
    country = models.CharField(max_length=35, blank=True, null=True, verbose_name='страна', help_text='Введите страну')
    avatar = models.ImageField(upload_to="users/avatar", blank=True, null=True, verbose_name='аватар',
                               help_text='Загрузите аватар')

    token = models.CharField(max_length=100, verbose_name='Токен', blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
