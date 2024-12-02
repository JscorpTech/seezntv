from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny

from core.apps.content.models.genre import GenreList
from core.apps.content.serializers.genre import GenreListSerializer


class GenresListAPIView(generics.ListCreateAPIView):
    pagination_class = None
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = GenreList.objects.all()
    serializer_class = GenreListSerializer

    permission_classes = [AllowAny]
