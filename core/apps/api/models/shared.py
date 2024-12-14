from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


from django_core.models import AbstractBaseModel


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
    image = models.ImageField(verbose_name=_("image"), upload_to="cadr/", max_length=255)
    content = models.ForeignKey("ContentModel", on_delete=models.CASCADE, null=True, related_name="cadrs")

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
    content = models.ForeignKey("ContentModel", verbose_name=_("content"), on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Object {self.id}"

    class Meta:
        db_table = "interval"
        verbose_name = _("IntervalModel")
        verbose_name_plural = _("IntervalModels")


class CommentModel(AbstractBaseModel):
    text = models.TextField(verbose_name=_("text"))
    user = models.ForeignKey(get_user_model(), verbose_name=_("user"), on_delete=models.CASCADE)
    content = models.ForeignKey("ContentModel", verbose_name=_("content"), on_delete=models.CASCADE)
    parent = models.ForeignKey("CommentModel", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.text

    class Meta:
        db_table = "comment"
        verbose_name = _("CommentModel")
        verbose_name_plural = _("CommentModels")
