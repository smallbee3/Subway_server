from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import UserSerializer, FacebookAccessTokenSerializer


__all__ = (
    'UserFacebookAccessTokenView',
)


class UserFacebookAccessTokenView(APIView):
    def post(self, request):
        serializer = FacebookAccessTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        return Response(UserSerializer(user).data)
