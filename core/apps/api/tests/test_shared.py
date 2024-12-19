from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from ..models import CategoryModel, GenreModel, TagModel, CommentModel
from ..serializers.shared import (
    ListCategorySerializer,
    RetrieveCategorySerializer,
    ListGenreSerializer,
    RetrieveGenreSerializer,
    ListTagSerializer,
    RetrieveTagSerializer,
    ListCommentSerializer,
)
from .base import BaseTestCase
from django.contrib.auth import get_user_model


class SharedViewsTest(APITestCase, BaseTestCase):

    def setUp(self):
        self.client = APIClient()
        self.content = self._create_film()
        self.user = get_user_model().objects.create_user(username="test", phone="998888112309", password="test")
        self.category = CategoryModel.objects.create(name="Test Category", position=1)
        self.genre = GenreModel.objects.create(name="Test Genre")
        self.tag = TagModel.objects.create(name="Test Tag")
        self.comment = CommentModel.objects.create(text="Test Comment", user=self.user, content_id=self.content.id)

    def test_category_list(self):
        url = reverse("category-list")
        response = self.client.get(url)
        categories = CategoryModel.objects.all()
        serializer = ListCategorySerializer(categories, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"status": True, "data": serializer.data})

    def test_category_retrieve(self):
        url = reverse("category-detail", kwargs={"pk": self.category.pk})
        response = self.client.get(url)
        category = CategoryModel.objects.get(pk=self.category.pk)
        serializer = RetrieveCategorySerializer(category)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"status": True, "data": serializer.data})

    def test_genre_list(self):
        url = reverse("genre-list")
        response = self.client.get(url)
        genres = GenreModel.objects.all()
        serializer = ListGenreSerializer(genres, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"status": True, "data": serializer.data})

    def test_genre_retrieve(self):
        url = reverse("genre-detail", kwargs={"pk": self.genre.pk})
        response = self.client.get(url)
        genre = GenreModel.objects.get(pk=self.genre.pk)
        serializer = RetrieveGenreSerializer(genre)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"status": True, "data": serializer.data})

    def test_tag_list(self):
        url = reverse("tag-list")
        response = self.client.get(url)
        tags = TagModel.objects.all()
        serializer = ListTagSerializer(tags, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"status": True, "data": serializer.data})

    def test_tag_retrieve(self):
        url = reverse("tag-detail", kwargs={"pk": self.tag.pk})
        response = self.client.get(url)
        tag = TagModel.objects.get(pk=self.tag.pk)
        serializer = RetrieveTagSerializer(tag)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"status": True, "data": serializer.data})

    def test_comment_create(self):
        url = reverse("comment-list")
        data = {"text": "New Comment", "user": self.comment.user_id, "content": self.comment.content_id}
        self.client.force_authenticate(user=self.comment.user)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CommentModel.objects.count(), 2)

    def test_comment_list(self):
        url = reverse("comment-detail", kwargs={"pk": self.content.id})
        response = self.client.get(url)
        comment = CommentModel.objects.filter(content=self.content)
        serializer = ListCommentSerializer(comment, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data']['results'], serializer.data)
