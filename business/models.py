from django.db import models

from core.models import User


class SellerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.SELLER)


class Seller(User):
    base_type = User.Types.SELLER
    objects = SellerManager()

    class Meta:
        proxy = True


class SellerData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_verified = models.BooleanField('Подтверждён', default=False)

    class Meta:
        verbose_name = 'Продавец'
        verbose_name_plural = 'Продавец'
