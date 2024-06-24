from django.contrib import admin
from django.template.defaultfilters import truncatechars

from forum.models import ProductMessage, FloodMessage


@admin.register(FloodMessage)
class FloodMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'category', 'universe', 'short_message')
    fields = ('user', 'category', 'universe', 'message')

    def short_message(self, obj):
        return truncatechars(obj.message, 35)
    short_message.short_description = 'Сообщение'


@admin.register(ProductMessage)
class ProductMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'upvotes_count', 'short_message')
    fields = ('user', 'product', 'message', 'users_upvotes', 'users_downvotes',)
    filter_horizontal = ('users_upvotes', 'users_downvotes',)

    def upvotes_count(self, obj):
        return obj.users_upvotes.count() - obj.users_downvotes.count()
    upvotes_count.short_description = 'Рейтинг'

    def short_message(self, obj):
        return truncatechars(obj.message, 35)
    short_message.short_description = 'Отзыв'
