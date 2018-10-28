import urllib

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.core.cache import cache
from django.db.models import Count
from django_filters import FilterSet, Filter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

from rest_framework import generics, permissions

from ingredients.models import Sandwich
from utils.permission.custom_permission import IsRecipeInventorOrReadOnly

from ..serializers.recipe import RecipeSerializer
from ..models import Recipe

User = get_user_model()

__all__ = (
    'RecipeListCreateView',
    'RecipeRetrieveUpdateDestroyView',
)


class ListFilter(Filter):
    def filter(self, qs, value):
        if not value:
            return qs

        self.lookup_expr = 'in'
        # value = urllib.parse.unquote_plus(value)
        value = value.replace(', ', '_ ')
        values_text = value.split(',')
        values = []
        for value in values_text:
            value = value.replace('_ ', ', ')
            obj = Sandwich.objects.get(name=value)
            values.append(obj.id)
        return super().filter(qs, values)


class RecipeFilter(FilterSet):
    sandwich = ListFilter()

    class Meta:
        model = Recipe
        fields = (
            'sandwich',
        )


class RecipeListCreateView(generics.ListCreateAPIView):

    # queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )

    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)

    # filtering
    # filter_fields = ('sandwich',)
    # DjangoFilterBackends에 multiple id를 사용하기 위해
    # filter_class와 ListFilter를 활용하여 Custom
    filter_class = RecipeFilter

    # ordering
    ordering_fields = ('id', 'like_count', 'bookmark_count', 'created_date',)
    ordering = ('-like_bookmark_count', '-bookmark_count', '-like_count',)

    # searching
    search_fields = ('name__name',)

    def get_queryset(self):

        # value = cache.get('recipes_detail')
        # if not value:
        value = Recipe.objects \
            .select_related('name__user', 'sandwich', 'bread', 'cheese', 'toasting', 'inventor') \
            .prefetch_related('toppings', 'vegetables', 'sauces',
                              'sandwich__main_ingredient', 'sandwich__category',) \
            .annotate(
                    like_count=Count('liker', distinct=True),
                    bookmark_count=Count('bookmarker', distinct=True),
                    like_bookmark_count=Count('liker', distinct=True)
                                        + Count('bookmarker', distinct=True),
            )
            # value = cache.get_or_set('recipes_detail', value, 300)

        return value

    def get_serializer_context(self):
        context = super().get_serializer_context()

        # get_serializer_context 작동 테스트 코드
        # context['request'].user = AnonymousUser()
        return context

    def perform_create(self, serializer):
        serializer.save(inventor=self.request.user)


class RecipeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    # queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsRecipeInventorOrReadOnly,
    )

    def get_queryset(self):

        # value = cache.get('recipes_detail')
        # if not value:
        value = Recipe.objects \
            .select_related('name__user', 'sandwich', 'bread', 'cheese', 'toasting', 'inventor') \
            .prefetch_related('toppings', 'vegetables', 'sauces',
                              'sandwich__main_ingredient', 'sandwich__category',) \
            .annotate(
                    like_count=Count('liker', distinct=True),
                    bookmark_count=Count('bookmarker', distinct=True),
                    like_bookmark_count=Count('liker', distinct=True)
                                        + Count('bookmarker', distinct=True),
            )
            # value = cache.get_or_set('recipes_detail', value, 300)

        return value
