from rest_framework import serializers
from dj_rest_auth.serializers import UserDetailsSerializer


class CurrentUserSerializer(UserDetailsSerializer):
    """
    A class for the CurrentUserSerializer user details serializer
    """
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta(UserDetailsSerializer.Meta):
        """
        Returns profile_id and profile_image values of the logged in user
        """
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image',
            )