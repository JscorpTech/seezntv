from ..models import ContentModel, GenreModel, TagModel, CategoryModel, MediaModel, BannerModel
from django.test import TestCase


class BaseTestCase(TestCase):

    def _create_banner(self):
        content = self._create_film()
        return BannerModel.objects.create(
            film=content,
            content="Banner content",
            position=1,
        )

    def _create_film(self):
        content = ContentModel.objects.create(
            title="Film title",
            description="Film description",
            release_date="2022-01-01",
            age_limit=16,
            poster_desktop="poster_desktop.jpg",
            poster_mobile="poster_mobile.jpg",
            poster_card="poster_card.jpg",
            poster_video="poster_video.mp4",
        )
        genre = GenreModel.objects.create(name="Genre name")
        content.genre.add(genre)
        tag = TagModel.objects.create(name="Tag name")
        content.tags.add(tag)
        category = CategoryModel.objects.create(name="Category name")
        content.category.add(category)
        media = MediaModel.objects.create(name="Media name")
        content.ova.add(media)
        content.chronology.add(media)
        return content
