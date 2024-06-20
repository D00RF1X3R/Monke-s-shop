from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import SET_DEFAULT

from business.models import Seller
from core.models import Category, Universe


def get_default_category():
    return Category.objects.get_or_create(name='Прочее')


def get_default_universe():
    return Universe.objects.get_or_create(name='Прочее')


class Product(models.Model):
    name = models.CharField('Наименование', max_length=250)
    seller = models.ForeignKey(Seller, verbose_name='Продавец', on_delete=models.CASCADE)

    # category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    # universe = models.ForeignKey(Universe, verbose_name='Категория', on_delete=models.CASCADE)

    category = models.ForeignKey(Category, verbose_name='Категория', default=get_default_category, on_delete=SET_DEFAULT)
    universe = models.ForeignKey(Universe, verbose_name='Вселенная', default=get_default_universe, on_delete=SET_DEFAULT)

    preview = models.ImageField('Превью', upload_to='uploads/', null=True, blank=True)
    description = models.CharField('Описание', max_length=2000)
    price = models.IntegerField('Цена', validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.CASCADE)
    image = models.ImageField('Изображение', upload_to='uploads/', null=True, blank=True)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
