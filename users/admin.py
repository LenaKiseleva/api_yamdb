from django.contrib import admin
from import_export.admin import ImportMixin

from .models import User
from .resources import UserResource


class UserAdmin(ImportMixin, admin.ModelAdmin):
    resource_class = UserResource
    list_display = ("role",)


admin.site.register(User, UserAdmin)
