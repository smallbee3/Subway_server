import re

from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status

from utils.exceptions import CustomAPIException
from utils.permission.custom_permission import IsOwnerOrReadOnly
from ..models import Collection
from ..serializers.collection import BookmarkCollectionSerializer

from utils.exceptions.get_object_or_404 import get_object_or_404_customed

User = get_user_model()


class BookmarkCollectionListCreateView(generics.ListCreateAPIView):
    # queryset = Collection.objects.all()
    serializer_class = BookmarkCollectionSerializer

    permission_classes = (
        permissions.IsAuthenticated,
        IsOwnerOrReadOnly,
    )

    def get_queryset(self):
        user = get_object_or_404_customed(User, pk=self.kwargs['pk'])
        value = Collection.objects.all().filter(user=user)
        return value

    def perform_create(self, serializer):
        # user = get_object_or_404_customed(User, pk=self.kwargs['pk'])
        # serializer.save(user=user)
        user = self.request.user
        serializer.save(user=user)


class BookmarkCollectionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Collection.objects.all()
    serializer_class = BookmarkCollectionSerializer

    permission_classes = (
        permissions.IsAuthenticated,
        IsOwnerOrReadOnly,
    )

    def get_queryset(self):
        path = self.request._request.path
        result = re.search(r'.+?(\d+).+?', path)
        pk = result.group(1)
        user = get_object_or_404_customed(User, pk=pk)
        if not user == self.request.user:
            raise CustomAPIException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Authenticated user and user from request uri do not match",
                request_user_pk=self.request.user.pk
            )
        value = Collection.objects.all().filter(user=self.request.user)
        return value
