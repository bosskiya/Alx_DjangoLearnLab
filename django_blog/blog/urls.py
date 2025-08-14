from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .models import Post
from .views import SearchResultsView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentUpdateView, CommentDeleteView, CommentCreateView
from taggit.models import Tag
from django.shortcuts import get_object_or_404, render

# Tag filtered posts view
def PostByTagListView(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = Post.objects.filter(tags__slug__in=[tag_slug])
    return render(request, 'blog/posts_by_tag.html', {'tag': tag, 'posts': posts})

urlpatterns = [
    # Auth URLs
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),

    # Blog post URLs
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Comment URLs
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

    path('search/', SearchResultsView.as_view(), name='post-search'),
    path('tags/<slug:tag_slug>/', PostByTagListView, name='posts-by-tag'),
]
