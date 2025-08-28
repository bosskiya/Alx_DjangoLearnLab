from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import permissions
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from notifications.utils import create_notification

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def user_feed(request):
    following_users = request.user.following.all()
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response({'error': 'Post not found'}, status=404)

    if Like.objects.filter(user=request.user, post=post).exists():
        return Response({'message': 'You have already liked this post.'}, status=400)

    Like.objects.create(user=request.user, post=post)

    # Create notification
    if request.user != post.author:
        create_notification(
            recipient=post.author,
            actor=request.user,
            verb='liked your post',
            target=post
        )

    return Response({'message': 'Post liked.'})

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unlike_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response({'error': 'Post not found'}, status=404)

    like = Like.objects.filter(user=request.user, post=post).first()
    if not like:
        return Response({'message': 'You have not liked this post.'}, status=400)

    like.delete()
    return Response({'message': 'Post unliked.'})


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)