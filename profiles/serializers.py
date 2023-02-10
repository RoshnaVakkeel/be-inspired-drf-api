from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    '''
    Serializer for Profile Model data
    '''
    # fetches user's username
    owner = serializers.ReadOnlyField(source='owner.username') 

    class Meta:
        '''
        Metadata for Profile Serializer
        '''
        model = Profile
        fields = [
            'id', 'owner', 'created_on', 'updated_on', 'name',
            'brief_bio', 'age_group', 'image',
        ]
