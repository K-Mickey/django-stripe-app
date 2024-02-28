from django.db import models


class CurrencyType(models.TextChoices):
    RUB = 'RUB', 'Рубль'
    USD = 'USD', 'Доллар'
    EUR = 'EUR', 'Евро'


class Item(models.Model):
    name = models.CharField(
        verbose_name='Наименование',
        max_length=255,
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена',
        default=0,
    )
    currency = models.CharField(
        verbose_name='Валюта',
        max_length=3,
        choices=CurrencyType.choices,
        default=CurrencyType.USD,
    )

    def __str__(self):
        return f'{self.name} - {self.price} {self.currency}'
