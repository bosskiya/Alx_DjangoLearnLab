from django.contrib import admin
from .models import Book, CustomUser
from django import forms
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


class ModelAdmin(admin.ModelAdmin):
    list_display = ("list_filter", "author", "publication_year")
    search_fields = ('title', 'author')


class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'date_of_birth', 'profile_photo')


class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'date_of_birth', 'profile_photo', 'is_active', 'is_staff')


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ('username', 'email', 'date_of_birth', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    fieldsets = ((None, {'fields': ('username', 'email', 'password')}),
        (_('Personal info'), {'fields': ('date_of_birth', 'profile_photo')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = ((None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'date_of_birth', 'profile_photo', 'is_staff'),
        }),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(Book, ModelAdmin)
admin.site.register(CustomUser, CustomUserAdmin)