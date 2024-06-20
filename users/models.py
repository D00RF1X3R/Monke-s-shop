from django.core.validators import MinValueValidator
from django.db import models

from catalog.models import Product
from core.models import User, Universe, Category
from core.validators import RangeValidator


class CustomerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.CUSTOMER)


class Customer(User):
    base_type = User.Types.CUSTOMER
    objects = CustomerManager()

    class Meta:
        proxy = True


class CustomerData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField('Баланс', validators=[MinValueValidator(0)], default=0)
    favorite_universes = models.ManyToManyField(Universe)
    favorite_categories = models.ManyToManyField(Category)
    favorite_products = models.ManyToManyField(Product)

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField('Кол-во', validators=[MinValueValidator(1)], default=1)

    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'


class BuyHistory(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField('Кол-во', validators=[MinValueValidator(1)], default=1)
    date = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'История покупки'
        verbose_name_plural = 'Истории покупок'


class Rating(models.Model):
    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.CASCADE)
    user = models.ForeignKey(Customer, verbose_name='Покупатель', on_delete=models.CASCADE)
    mark = models.IntegerField('Оценка', validators=[RangeValidator(0, 5)])

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'
