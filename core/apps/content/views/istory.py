from rest_framework import generics
from rest_framework.permissions import AllowAny

from core.apps.content.models.istory import Istory
from core.apps.content.serializers.istory import IstorySerializer


class IstoryListAPIView(generics.ListCreateAPIView):
    queryset = Istory.objects.filter().order_by("-id")
    serializer_class = IstorySerializer

    permission_classes = [AllowAny]
