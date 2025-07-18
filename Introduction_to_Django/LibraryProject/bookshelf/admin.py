from django.contrib import admin
from .models import Book


class ModelAdmin(admin.ModelAdmin):
    list_display = ("list_filter", "author", "publication_year")
    search_fields = ('title', 'author')
admin.site.register(Book, ModelAdmin)