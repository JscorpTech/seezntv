from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny

from core.apps.content.models.category import CategoryList
from core.apps.content.serializers.category import CategoryListSerializer


class CategoryListAPIView(generics.ListCreateAPIView):
    pagination_class = None
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = CategoryList.objects.all()
    serializer_class = CategoryListSerializer

    permission_classes = [AllowAny]
