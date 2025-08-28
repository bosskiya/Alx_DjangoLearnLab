from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, user_feed, like_post, unlike_post

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', user_feed, name='user-feed'),
    path('posts/<int:pk>/like/', like_post),
    path('posts/<int:pk>/unlike/', unlike_post),
]