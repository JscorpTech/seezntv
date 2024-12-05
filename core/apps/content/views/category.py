from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny

from core.apps.content.models.category import Category
from core.apps.content.serializers.category import CategoryListSerializer


class CategoryListAPIView(generics.ListCreateAPIView):
    pagination_class = None
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer

    permission_classes = [AllowAny]
