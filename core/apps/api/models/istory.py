from django.db import models
from django.utils.translation import gettext_lazy as _

from core.http.models import AbstractBaseModel


class IstoryModel(AbstractBaseModel):
    content = models.CharField(verbose_name=_("content"), max_length=255)
    videos = models.ManyToManyField("IstoryVideoModel")

    def __str__(self):
        return self.content

    class Meta:
        db_table = "istory"
        verbose_name = _("IstoryModel")
        verbose_name_plural = _("IstoryModels")


class IstoryVideoModel(AbstractBaseModel):
    video = models.FileField(verbose_name=_("video"), upload_to="video/")

    def __str__(self):
        return self.video

    class Meta:
        db_table = "istoryvideo"
        verbose_name = _("IstoryvideoModel")
        verbose_name_plural = _("IstoryvideoModels")
