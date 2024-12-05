from django.db import models
from django.utils.translation import gettext_lazy as _

from core.http.models import AbstractBaseModel


class MediaModel(AbstractBaseModel):
    video = models.CharField(verbose_name=_("video"), max_length=255)
    name = models.CharField(verbose_name=_("name"), max_length=255, null=True, blank=True)
    skip_start_time = models.DurationField(verbose_name=_("skip_start_time"), null=True, blank=True)
    skip_end_time = models.DurationField(verbose_name=_("skip_end_time"), null=True, blank=True)

    position = models.PositiveIntegerField(verbose_name=_("position"), null=True, blank=True)

    def __str__(self) -> str:
        return "id: %s name: %s" % (self.id, self.name)

    class Meta:
        ordering = ["-position"]
        db_table = "media"
        verbose_name = _("MediaModel")
        verbose_name_plural = _("MediaModels")
