from django.db.models import Count
from rest_framework import generics, permissions, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from be_inspired_dr_api.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    '''
    Lists all the created profiles
    '''
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        recommendations_count=Count('owner__recommendation', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_on')

    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = [
        'posts_count',
        'recommendations_count',
        'followers_count',
        'following_count',
        'owner__following__created_on',
        'owner__followed__created_on',
    ]
    search_fields = [
        'owner__username',
        'name',
        'age_group',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    '''
    Displays details of selected profile
    Allows the owner to edit it
    '''
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        recommendations_count=Count('owner__recommendation', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_on')
