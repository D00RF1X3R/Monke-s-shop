from django.db import models

from catalog.models import Product
from core.models import User, Category, Universe


class BaseMessage(models.Model):
    user = models.ForeignKey(User, verbose_name='user', on_delete=models.CASCADE)
    message = models.CharField('Сообщение', max_length=1000)

    class Meta:
        abstract = True


class FloodMessage(BaseMessage):
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    universe = models.ForeignKey(Universe, verbose_name='Вселенная', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class ProductMessage(BaseMessage):
    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.CASCADE)
    users_upvotes = models.ManyToManyField(User, verbose_name='upvotes', related_name='upvotes')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
