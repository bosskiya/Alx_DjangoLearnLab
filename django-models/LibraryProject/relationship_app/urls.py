from django.urls import path
from .views import list_books, LibraryDetailView, admin_view, librarian_view, member_view, add_book, edit_book, delete_book
from relationship_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),

    path('admin-dashboard/', admin_view, name="admin-view"),
    path('librarian-dashboard/', librarian_view, name="librarian-view"),
    path('member-dashboard/', member_view, name="member-view"),

    path('books/add/', add_book, name='add-book'),
    path('books/edit/<int:pk>/', edit_book, name='edit-book'),
    path('books/delete/<int:pk>/', delete_book, name='delete-book'),
]
