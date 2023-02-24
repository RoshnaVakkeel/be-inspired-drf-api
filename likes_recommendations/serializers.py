from django.db import IntegrityError
from rest_framework import serializers
from .models import LikeRecommendation


class LikeRecommendationSerializer(serializers.ModelSerializer):
    '''
    Class for LikeRecommendation Serializer
    '''
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = LikeRecommendation
        fields = ['id', 'owner', 'created_on','recommendation',]

    def create(self, validated_data):
        '''
        Handles duplicated likes by the same user
        '''
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplication'
            })
