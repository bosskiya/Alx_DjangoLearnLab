from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        permissions = [
            ("can_add_book", "can add book"),
            ("can_change_book", "can edit book"),
            ("can_delete_book", "can delete book")
        ]


class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name


class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    Role_choice = [
        ("Admin", "Admin"),
        ("Librarian", "Librarian"),
        ("Member", "Member")
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=Role_choice)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()