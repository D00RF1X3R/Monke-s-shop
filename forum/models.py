from django.db import models

from catalog.models import Product
from core.models import User, Category, Universe


class BaseMessage(models.Model):
    user = models.ForeignKey(User, verbose_name='user', on_delete=models.CASCADE)
    message = models.TextField('Сообщение')

    class Meta:
        abstract = True


class FloodMessage(BaseMessage):
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    universe = models.ForeignKey(Universe, verbose_name='Вселенная', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return f'Сообщение #{self.id}'


class ProductMessage(BaseMessage):
    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.CASCADE)
    users_upvotes = models.ManyToManyField(User, verbose_name='Апвоуты', related_name='upvotes', blank=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'Отзыв #{self.id}'