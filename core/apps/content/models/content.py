from django.db import models

from core.apps.content.models.cadr import Cadr
from core.apps.content.models.category import Category
from core.apps.content.models.genre import Genre
from core.apps.content.models.tag import Tag
from core.apps.content.models.video import VideoContent


class Content(models.Model):
    """
    Main Video content model for movie,serias, anime ...
    """

    poster_desktop = models.URLField()
    poster_mobile = models.URLField()
    poster_card = models.URLField()
    poster_video = models.URLField()

    title = models.CharField(max_length=300)

    kadrs = models.ManyToManyField(Cadr, blank=True)
    genre = models.ManyToManyField(Genre)
    category = models.ManyToManyField(Category)
    description = models.TextField()

    contents = models.ManyToManyField(VideoContent, related_name="contents")
    ova = models.ManyToManyField(VideoContent, blank=True, related_name="ova")
    chronology = models.ManyToManyField(VideoContent, blank=True, related_name="chronology")

    age_limit = models.PositiveIntegerField()

    release_date = models.DateField()
    tags = models.ManyToManyField(Tag, blank=True)

    upload_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
