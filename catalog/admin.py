from django.contrib import admin
from catalog.models import Product, ProductImage
from django.template.defaultfilters import truncatechars


class ProductImageInlined(admin.StackedInline):
    model = ProductImage
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'universe', 'short_description')
    fields = ('name', 'seller', 'category', 'universe', 'preview', 'description', 'price')
    inlines = (ProductImageInlined,)

    def short_description(self, obj):
        return truncatechars(obj.description, 35)
    short_description.short_description = 'Описание'
