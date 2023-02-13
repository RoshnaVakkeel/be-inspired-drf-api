from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer
from be_inspired_dr_api.permissions import IsOwnerOrReadOnly


class PostList(generics.ListAPIView):
    '''
    Lists all the created posts
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
        'owner__followed__owner__profile',
        'likes__owner__profile',
        'owner__profile',
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
