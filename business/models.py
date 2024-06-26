from django.contrib.auth.models import UserManager
from django.db import models

from core.models import User


class SellerManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.SELLER)


class Seller(User):
    base_type = User.Types.SELLER
    objects = SellerManager()

    class Meta:
        proxy = True
        verbose_name = 'Продавец'
        verbose_name_plural = 'Продавцы'


class SellerData(models.Model):
    user = models.OneToOneField(Seller, on_delete=models.CASCADE)
    is_verified = models.BooleanField('Подтверждён', default=False)

    def __str__(self):
        return self.user.username