from django.contrib import admin
from .models import Book


class ModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(Book, ModelAdmin)