from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Recommendation
from .serializers import RecommendationSerializer
from be_inspired_dr_api.permissions import IsOwnerOrReadOnly


class RecommendationList(generics.ListCreateAPIView):
    '''
    Lists all the created Recommendations
    '''
    serializer_class = RecommendationSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Recommendation.objects.annotate(
        comments_count=Count('comment', distinct=True),
        likes_count=Count('likes', distinct=True),
    ).order_by('-created_on')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',  # return user's recommendations
        'likes__owner__profile',  # return recommendations a user liked
        'owner__profile',  # return recommendations owned by a specific user
        'category',  # return which category the recommendation belongs to
    ]
    ordering_fields = [
        'comments_count',
        'likes_count',
        'likes__created_on',
    ]
    search_fields = [
        'title',
        'category',
        'price_category',
        'description',
        'reason',
    ]

    def perform_create(self, serializer):
        '''
        Asociates the Recommendation with the user creating Recommendation
        '''
        serializer.save(owner=self.request.user)


class RecommendationDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Displays details of selected Recommendation
    Allows the owner to edit or delete it
    '''
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = RecommendationSerializer
    queryset = Recommendation.objects.annotate(
        comments_count=Count('comment', distinct=True),
        likes_count=Count('likes', distinct=True),
    ).order_by('-created_on')
