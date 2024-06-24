from django.contrib.auth.models import AbstractUser
from django.db import models

class Category(models.Model):
    name = models.CharField('Название', max_length=50)
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Universe(models.Model):
    name = models.CharField('Название', max_length=50)
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вселенная'
        verbose_name_plural = 'Вселенные'


class User(AbstractUser):
    class Types(models.TextChoices):
        CUSTOMER = 'Покупатель', 'ПОКУПАТЕЛЬ'
        SELLER = 'Продавец', 'ПРОДАВЕЦ'

    base_type = Types.CUSTOMER
    type = models.CharField('Тип', max_length=15, choices=Types.choices, default=base_type)
    image = models.ImageField('Иконка', upload_to='uploads/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.type = self.base_type
        return super().save(*args, **kwargs)
    
