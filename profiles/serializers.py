from rest_framework import serializers
from .models import Profile
from followers.models import Follower


class ProfileSerializer(serializers.ModelSerializer):
    '''
    Serializer for Profile Model data
    '''
    # fetches user's username
    owner = serializers.ReadOnlyField(source='owner.username') 
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    recommendations_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
    # checks if the logged in user  is following any other profiles
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return following.id if following else None
        return None

    class Meta:
        '''
        Metadata for Profile Serializer
        '''
        model = Profile
        fields = [
            'id', 'owner', 'created_on', 'updated_on', 'name',
            'brief_bio', 'age_group', 'image', 'is_owner', 'following_id',
            'posts_count', 'recommendations_count',
            ]
