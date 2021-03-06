from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from bookmarkcollection.models import Collection
from users.serializers import UserSerializer
from utils.exceptions.get_object_or_404 import get_object_or_404_customed
from ..models import Recipe, Bookmark

__all__ = (
    'BookmarkListCreateView',
)


class BookmarkListCreateView(APIView):

    def post(self, request, pk):
        user = request.user
        recipe = get_object_or_404_customed(Recipe, pk=pk)
        instance, created = Bookmark.objects.get_or_create(
            recipe=recipe,
            user=user,
        )

        # 2018.11.11
        # Get or create default collection
        #  and connect it with bookmark instance which was newly made above
        if created:
            collection, _ = Collection.objects.get_or_create(
                name='default',
                user=user
            )
            instance.collection = collection
            instance.save()

        if not created:
            instance.delete()
            return Response(
                f'User(id:{user.pk})가 recipe(id:{recipe.pk})의 저장을 취소했습니다.',
                status=status.HTTP_204_NO_CONTENT,
            )
        else:
            return Response(
                f'User(id:{user.pk})가 recipe(id:{recipe.pk})를 저장했습니다.',
                status=status.HTTP_200_OK,
            )

    def get(self, request, pk):
        recipe = get_object_or_404_customed(Recipe, pk=pk)
        bookmarkers = recipe.bookmarker.all()
        serializer = UserSerializer(bookmarkers, many=True, context=self.request)
        return Response(serializer.data)
