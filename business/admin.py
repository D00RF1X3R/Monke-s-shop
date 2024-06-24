from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from business.models import Seller, SellerData


class SellerInlined(admin.StackedInline):
    model = SellerData
    can_delete = False
    min_num = 1
    max_num = 1
    extra = 1

    fields = ('is_verified',)
    verbose_name = 'Информация о продавце'


@admin.register(Seller)
class CustomerAdmin(UserAdmin):
    list_display = ('id', 'username', 'is_verified')

    fieldsets = UserAdmin.fieldsets + (
        ('Информация аккаунта', {
            'fields': ('type', 'image')
        }),
    )
    inlines = (SellerInlined,)

    def is_verified(self, obj):
        if SellerData.objects.get_or_create(user=obj.id)[0].is_verified:
            return 'Да'
        return 'Нет'
    is_verified.short_description = 'Подтверждён'
