from django.db import models
from django.utils.translation import gettext_lazy as _

from core.http.models import AbstractBaseModel


class BannerModel(AbstractBaseModel):
    content = models.CharField(_("content"), max_length=255)
    film = models.ForeignKey(verbose_name=_("film"), to="ContentModel", on_delete=models.CASCADE)
    position = models.PositiveIntegerField(_("position"), default=0)

    def __str__(self):
        return self.content

    class Meta:
        db_table = "banner"
        verbose_name = _("BannerModel")
        verbose_name_plural = _("BannerModels")
        ordering = ['position']
