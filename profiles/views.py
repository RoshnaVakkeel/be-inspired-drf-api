from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from be_inspired_dr_api.permissions import IsOwnerOrReadOnly

# DRF-API walkthrough steps have been referred at each step

class ProfileList(generics.ListAPIView):
    '''
    Lists all the created profiles
    '''
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()


class ProfileDetail(generics.RetrieveUpdateAPIView):
    '''
    Displays details of selected profile and allows the owner to edit it
    '''
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
