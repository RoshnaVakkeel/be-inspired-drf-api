from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer
from be_inspired_dr_api.permissions import IsOwnerOrReadOnly


class PostList(generics.ListCreateAPIView):
    '''
    Lists all the created posts
    The perform_create method associates the post with the logged in user.
    '''
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Post.objects.annotate(
        comments_count=Count('comment', distinct=True),
        likes_count=Count('likes', distinct=True),
    ).order_by('-created_on')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',  # return specific user's posts
        'likes__owner__profile',  # return posts a specific user liked
        'owner__profile',  # return posts owned by a specific user
        'category',  # return which category the post belongs to
    ]
    ordering_fields = [
        'comments_count',
        'likes_count',
        'likes__created_on',
    ]
    search_fields = [
        'title',
        'category',
        'description',
    ]

    def perform_create(self, serializer):
        '''
        Asociates the post with the user creating post
        '''
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Displays details of selected post
    Allows the owner to edit or delete it
    '''
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.annotate(
        comments_count=Count('comment', distinct=True),
        likes_count=Count('likes', distinct=True),
    ).order_by('-created_on')
