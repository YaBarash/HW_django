# Generated by Django 5.1 on 2024-10-04 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_product_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['category', 'name'], 'permissions': [('set_published', 'Can publish products'), ('change_description', 'Can change description'), ('change_category', 'Can change category')], 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AddField(
            model_name='product',
            name='publication',
            field=models.BooleanField(default=False, help_text='продукт опубликован', verbose_name='признак публикации продукта'),
        ),
    ]
