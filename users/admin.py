from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import Customer, CustomerData, Cart, BuyHistory, Rating
from django.contrib.auth.models import Group


admin.site.unregister(Group)


class CustomerInlined(admin.StackedInline):
    model = CustomerData
    can_delete = False
    min_num = 1
    max_num = 1
    extra = 1

    fields = ('balance', 'favorite_universes', 'favorite_categories', 'favorite_products')
    filter_horizontal = ('favorite_universes', 'favorite_categories', 'favorite_products')
    verbose_name = 'Информация о покупателе'


@admin.register(Customer)
class CustomerAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'balance')
    fieldsets = UserAdmin.fieldsets + (
        ('Информация аккаунта', {
            'fields': ('type', 'image')
        }),
    )
    inlines = (CustomerInlined,)

    def balance(self, obj):
        return CustomerData.objects.get_or_create(user=obj.id)[0].balance
    balance.short_description = 'Баланс'


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'product', 'count')
    fields = ('customer', 'product', 'count')


@admin.register(BuyHistory)
class BuyHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'product', 'count', 'date')
    fields = ('customer', 'product', 'count')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'mark')
    fields = ('user', 'product', 'mark')
