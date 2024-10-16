# Generated by Django 5.1 on 2024-10-06 07:43

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Введите имя', max_length=20, verbose_name='Имя')),
                ('last_name', models.CharField(help_text='Введите фамилию', max_length=35, verbose_name='Фамилия')),
                ('email', models.EmailField(help_text='Введите email', max_length=254, unique=True, verbose_name='Почта')),
                ('comment', models.TextField(blank=True, help_text='Укажите комментарий', null=True, verbose_name='Комментарий')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='EmailSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(blank=True, default=datetime.datetime(2024, 10, 6, 7, 43, 24, 341364, tzinfo=datetime.timezone.utc), null=True, verbose_name='Время старта')),
                ('stop_time', models.DateTimeField(blank=True, default=datetime.datetime(2024, 10, 13, 7, 43, 24, 341364, tzinfo=datetime.timezone.utc), null=True, verbose_name='Время окончания')),
                ('period', models.CharField(choices=[('daily', 'Ежедневная'), ('weekly', 'Раз в неделю'), ('monthly', 'Раз в месяц')], default='daily', max_length=20, verbose_name='Период')),
                ('status', models.CharField(choices=[('created', 'Создана'), ('started', 'Запущена'), ('done', 'Завершена')], default='created', max_length=20, verbose_name='Статус')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Настройка',
                'verbose_name_plural': 'Настройки',
            },
        ),
        migrations.CreateModel(
            name='MailingClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.client', verbose_name='клиент')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.emailsettings', verbose_name='рассылка')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Список рассылки',
                'verbose_name_plural': 'Списки рассылок',
            },
        ),
        migrations.CreateModel(
            name='MailingMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter_subject', models.CharField(max_length=100, verbose_name='Тема письма')),
                ('letter_body', models.TextField(verbose_name='Тело письма')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Письмо',
                'verbose_name_plural': 'Письма',
            },
        ),
        migrations.AddField(
            model_name='emailsettings',
            name='message',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.mailingmessage', verbose_name='Сообщение'),
        ),
        migrations.CreateModel(
            name='MailLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_attempt', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время последней попытки')),
                ('try_status', models.CharField(choices=[('ok', 'Успешно'), ('failed', 'Ошибка')], default='ok', verbose_name='Статус попытки')),
                ('mailing_service_response', models.TextField(blank=True, null=True, verbose_name='Ответ почтового сервера, если он был')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.client', verbose_name='Клиент')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.emailsettings', verbose_name='Рассылка')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Лог',
                'verbose_name_plural': 'Логи',
            },
        ),
    ]
