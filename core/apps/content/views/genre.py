from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny

from core.apps.content.models.genre import Genre
from core.apps.content.serializers.genre import GenreListSerializer


class GenresListAPIView(generics.ListCreateAPIView):
    pagination_class = None
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Genre.objects.all()
    serializer_class = GenreListSerializer

    permission_classes = [AllowAny]
