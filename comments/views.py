from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer
from be_inspired_dr_api.permissions import IsOwnerOrReadOnly


class CommentList(generics.ListCreateAPIView):
    '''
    Lists all the created Comments
    '''
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Comment.objects.all()
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner',
        'post',
        'recommendation',
    ]

    def perform_create(self, serializer):
        '''
        Asociates the Comment with the user creating Comment
        '''
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Displays details of selected Comment
    Allows the owner to edit/delete it
    '''
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()
