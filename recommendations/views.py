from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Recommendation
from .serializers import RecommendationSerializer
from be_inspired_dr_api.permissions import IsOwnerOrReadOnly


class RecommendationList(generics.ListAPIView):
    '''
    Lists all the created Recommendations
    '''
    serializer_class = RecommendationSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Recommendation.objects.all()

    def perform_create(self, serializer):
        '''
        Asociates the Recommendation with the user creating Recommendation
        '''
        serializer.save(owner=self.request.user)

class RecommendationDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Displays details of selected Recommendation and allows the owner to edit or delete it
    '''
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = RecommendationSerializer
    queryset = Recommendation.objects.all()
