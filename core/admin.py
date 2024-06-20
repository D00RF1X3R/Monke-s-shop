from django.contrib import admin

from core.models import Category, Universe


@admin.register(Universe)
class UniverseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    fields = ('name',)
