# Generated by Django 5.0.2 on 2024-02-28 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PaymentApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='currency',
            field=models.CharField(choices=[('RUB', 'Рубль'), ('USD', 'Доллар'), ('EUR', 'Евро')], default='USD', max_length=3, verbose_name='Валюта'),
        ),
    ]