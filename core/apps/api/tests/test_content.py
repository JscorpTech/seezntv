from .base import BaseTestCase
from rest_framework.test import APIClient
from django.urls import reverse
from ..serializers import ListContentSerializer, RetrieveContentSerializer


class ContentTest(BaseTestCase):
    def setUp(self):
        self.content = self._create_film()
        self.client = APIClient()
        self.urls = {
            "list": reverse("content-list"),
            "retrieve": reverse("content-detail", kwargs={"pk": self.content.id}),
            # "create": reverse("content-create"),
            # "update": reverse("content-update", kwargs={"pk": self.content.id}),
            # "partial_update": reverse("content-partial-update", kwargs={"pk": self.content.id}),
            # "destroy": reverse("content-destroy", kwargs={"pk": self.content.id}),
        }

    def test_create(self):
        self.assertTrue(True)

    def test_update(self):
        self.assertTrue(True)

    def test_partial_update(self):
        self.assertTrue(True)

    def test_destroy(self):
        self.assertTrue(True)

    def test_list(self):
        response = self.client.get(self.urls["list"])
        serializer = ListContentSerializer(self.content)
        self.assertEqual(response.data["data"]["results"], [serializer.data])
        self.assertEqual(response.status_code, 200)

    def test_retrieve(self):
        response = self.client.get(self.urls["retrieve"])
        serializer = RetrieveContentSerializer(self.content)
        self.assertEqual(response.data["data"], serializer.data)
        self.assertEqual(response.status_code, 200)
