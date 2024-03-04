from django.core.validators import MinValueValidator, MaxValueValidator
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
    price = models.FloatField(
        verbose_name='Цена',
        validators=[MinValueValidator(0.0)],
        default=0.0,
    )
    currency = models.CharField(
        verbose_name='Валюта',
        max_length=3,
        choices=CurrencyType.choices,
        default=CurrencyType.USD,
    )

    def __str__(self):
        return f'{self.name} - {self.price} {self.currency}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    @property
    def total_price(self):
        return int(self.price * 100)


class Order(models.Model):
    items = models.ManyToManyField(
        Item,
        verbose_name='Товары',
        related_name='orders',
    )
    currency = models.CharField(
        verbose_name='Валюта заказа',
        max_length=3,
        choices=CurrencyType.choices,
        default=CurrencyType.USD,
    )
    discount = models.ForeignKey(
        'Discount',
        verbose_name='Скидка',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    tax = models.ForeignKey(
        'Tax',
        verbose_name='Налог',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'Заказ No{self.id}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    @property
    def price(self):
        sum_items = sum(item.price for item in self.items.all())

        if self.discount:
            sum_items -= (sum_items * self.discount.percent) / 100
        if self.tax:
            sum_items += (sum_items * self.tax.percent) / 100

        return round(sum_items, 2)

    @property
    def total_price(self):
        return int(self.price * 100)


class Discount(models.Model):
    name = models.CharField(
        verbose_name='Название скидки',
        max_length=255,
    )
    percent = models.PositiveSmallIntegerField(
        verbose_name='Размер скидки',
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'


class Tax(models.Model):
    name = models.CharField(
        verbose_name='Название налога',
        max_length=255,
    )
    percent = models.PositiveSmallIntegerField(
        verbose_name='Размер налога',
        default=20,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Налог'
        verbose_name_plural = 'Налоги'
