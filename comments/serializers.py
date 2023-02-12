from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    '''
    Class for CommentSerializer for Comment model
    '''
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    created_on = serializers.SerializerMethodField()
    updated_on = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    # shows how long ago was the comment created or updated
    def get_created_on(self, obj):
        return naturaltime(obj.created_on)

    def get_updated_on(self, obj):
        return naturaltime(obj.updated_on)

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'post', 'profile_id', 'recommendation',
            'profile_image', 'created_on', 'updated_on',
            'content',
        ]
                   

class CommentDetailSerializer(CommentSerializer):
    '''
    Class for CommentDetailSerializer
    that inherits from the CommentSerializer
    '''
    post = serializers.ReadOnlyField(source='owner.post.id')
    recommendation = serializers.ReadOnlyField(
        source='owner.recommendation.id'
    )
