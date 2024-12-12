from django.db import models
from django.utils.translation import gettext_lazy as _

from core.http.models import AbstractBaseModel


class IstoryModel(AbstractBaseModel):
    content = models.TextField(verbose_name=_("content"))
    videos = models.ManyToManyField("IstoryVideoModel")
    position = models.PositiveIntegerField(_("position"), default=0)

    def __str__(self):
        return self.content

    class Meta:
        db_table = "istory"
        verbose_name = _("IstoryModel")
        verbose_name_plural = _("IstoryModels")
        ordering = ["position"]


class IstoryVideoModel(AbstractBaseModel):
    video = models.FileField(verbose_name=_("video"), upload_to="video/")

    def __str__(self):
        return self.video.name

    class Meta:
        db_table = "istoryvideo"
        verbose_name = _("IstoryvideoModel")
        verbose_name_plural = _("IstoryvideoModels")
