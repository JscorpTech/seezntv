from django.db import models
from django.utils.translation import gettext_lazy as _

from core.http.models import AbstractBaseModel


class ContentModel(AbstractBaseModel):
    """
    Main Video content model for movie,serias, anime ...
    """

    title = models.CharField(verbose_name=_("title"), max_length=300)
    description = models.TextField(verbose_name=_("description"))

    poster_desktop = models.ImageField(verbose_name=_("poster_desktop"), upload_to="poster/", max_length=255)
    poster_mobile = models.ImageField(verbose_name=_("poster_mobile"), upload_to="poster/", max_length=255)
    poster_card = models.ImageField(verbose_name=_("poster_card"), upload_to="poster/", max_length=255)
    poster_video = models.FileField(verbose_name=_("poster_video"), upload_to="poster/", max_length=255)

    genre = models.ManyToManyField(verbose_name=_("genre"), to="GenreModel")
    tags = models.ManyToManyField(verbose_name=_("tags"), to="TagModel", blank=True)
    category = models.ManyToManyField(verbose_name=_("category"), to="CategoryModel")

    ova = models.ManyToManyField(verbose_name=_("ova"), to="MediaModel", blank=True, related_name="ova")
    chronology = models.ManyToManyField(
        verbose_name=_("chronology"), to="MediaModel", blank=True, related_name="chronology"
    )

    age_limit = models.PositiveIntegerField(verbose_name=_("age_limit"))

    release_date = models.DateField(verbose_name=_("release_date"))

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = "content"
        verbose_name = _("ContentModel")
        verbose_name_plural = _("ContentModels")
