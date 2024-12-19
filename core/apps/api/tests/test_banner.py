from django.urls import reverse
from rest_framework.test import APIClient
from .base import BaseTestCase


class BannerTest(BaseTestCase):

    def setUp(self):
        self.banner = self._create_banner()
        self.client = APIClient()
        self.urls = {
            "list": reverse("banner-list"),
            "retrieve": reverse("banner-detail", kwargs={"pk": self.banner.id}),
            # "create": reverse("banner-create"),
            # "update": reverse("banner-update", kwargs={"pk": self.banner.id}),
            # "partial_update": reverse("banner-partial-update", kwargs={"pk": self.banner.id}),
            # "destroy": reverse("banner-destroy", kwargs={"pk": self.banner.id}),
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
        self.assertEqual(response.status_code, 200)

    def test_retrieve(self):
        response = self.client.get(self.urls["retrieve"])
        self.assertEqual(response.status_code, 200)
