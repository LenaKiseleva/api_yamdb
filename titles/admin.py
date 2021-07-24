from django.contrib import admin
from import_export.admin import ImportMixin

from titles.models import Category, Genre, Title

from .resources import CategoryResource, GenreResource, TitleResource


class CategoryAdmin(ImportMixin, admin.ModelAdmin):
    resource_class = CategoryResource
    list_display = ('id', 'name', 'slug')


class GenreAdmin(ImportMixin, admin.ModelAdmin):
    resource_class = GenreResource
    list_display = ('id', 'name', 'slug')


class TitleAdmin(ImportMixin, admin.ModelAdmin):
    resource_class = TitleResource
    list_display = ('id', 'name', 'year', 'description', 'category')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Title, TitleAdmin)
