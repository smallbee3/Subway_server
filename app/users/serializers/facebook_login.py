from rest_framework import serializers
from rest_framework.compat import authenticate

__all__ = (
    'FacebookAccessTokenSerializer',
)


class FacebookAccessTokenSerializer(serializers.Serializer):

    access_token = serializers.CharField()

    def validate(self, attrs):
        access_token = attrs.get('access_token')
        if access_token:
            user = authenticate(access_token=access_token)
            if not user:
                raise serializers.ValidationError('액세스 토큰이 올바르지 않습니다.')
        else:
            raise serializers.ValidationError('액세스 토큰이 필요합니다.')

        attrs['user'] = user
        return attrs
