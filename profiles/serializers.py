from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    '''
    Serializer for Profile Model data
    '''
    # fetches user's username
    owner = serializers.ReadOnlyField(source='owner.username') 
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        '''
        Metadata for Profile Serializer
        '''
        model = Profile
        fields = [
            'id', 'owner', 'created_on', 'updated_on', 'name',
            'brief_bio', 'age_group', 'image', 'is_owner',
        ]
