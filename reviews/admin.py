from django.contrib import admin
from import_export.admin import ImportMixin

from reviews.models import Comment, Review

from .resources import CommentResource, ReviewResource


class ReviewAdmin(ImportMixin, admin.ModelAdmin):
    resource_class = ReviewResource
    list_display = ('id', 'text', 'author', 'score', 'pub_date')


class CommentAdmin(ImportMixin, admin.ModelAdmin):
    resource_class = CommentResource
    list_display = ('id', 'text', 'author', 'pub_date')


admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
