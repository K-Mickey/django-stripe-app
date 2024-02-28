from django.db import models


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

    def __str__(self):
        return f'{self.name} - {self.price}'
