from django.db import models
from django.utils.translation import gettext_lazy as _

from core.http.models import AbstractBaseModel


class CategoryModel(AbstractBaseModel):
    name = models.CharField(verbose_name=_("name"), max_length=255)
    position = models.PositiveIntegerField(_("position"), default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "category"
        verbose_name = _("CategoryModel")
        verbose_name_plural = _("CategoryModels")
        ordering = ["position"]


class GenreModel(AbstractBaseModel):
    name = models.CharField(verbose_name=_("name"), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "genre"
        verbose_name = _("GenreModel")
        verbose_name_plural = _("GenreModels")


class CadrModel(AbstractBaseModel):
    image = models.FileField(verbose_name=_("image"), upload_to="cadr/", max_length=255)

    def __str__(self):
        return self.image.name

    class Meta:
        db_table = "cadr"
        verbose_name = _("CadrModel")
        verbose_name_plural = _("CadrModels")


class TagModel(AbstractBaseModel):
    name = models.CharField(verbose_name=_("name"), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "tag"
        verbose_name = _("TagModel")
        verbose_name_plural = _("TagModels")


class IntervalModel(AbstractBaseModel):
    items = models.ManyToManyField(verbose_name=_("items"), to="MediaModel")

    def __str__(self):
        return f"Object {self.id}"

    class Meta:
        db_table = "interval"
        verbose_name = _("IntervalModel")
        verbose_name_plural = _("IntervalModels")