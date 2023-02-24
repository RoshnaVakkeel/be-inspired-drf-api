from rest_framework import generics, permissions
from be_inspired_dr_api.permissions import IsOwnerOrReadOnly
from likes_recommendations.models import LikeRecommendation
from likes_recommendations.serializers import LikeRecommendationSerializer


class LikeRecommendationList(generics.ListCreateAPIView):
    '''
    A class for the LikeList generic API view
    '''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeRecommendationSerializer
    queryset = LikeRecommendation.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeRecommendationDetail(generics.RetrieveDestroyAPIView):
    '''
    Class for the LikeDetail generic API view
    Enables single like to be retrieved and deleted
    '''
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeRecommendationSerializer
    queryset = LikeRecommendation.objects.all()
