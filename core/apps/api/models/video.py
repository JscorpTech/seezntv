from django.db import models
from django.utils.translation import gettext_lazy as _

from core.http.models import AbstractBaseModel


class VideoModel(AbstractBaseModel):
    video = models.CharField(verbose_name=_("video"), max_length=255)
    name = models.CharField(verbose_name=_("name"), max_length=255, null=True, blank=True)
    content = models.ForeignKey(
        "ContentModel", verbose_name=_("content"), on_delete=models.CASCADE, related_name="contents"
    )
    skip_start_time = models.DurationField(verbose_name=_("skip_start_time"), null=True, blank=True)
    skip_end_time = models.DurationField(verbose_name=_("skip_end_time"), null=True, blank=True)

    position = models.PositiveIntegerField(verbose_name=_("position"), null=True, blank=True)

    def __str__(self):
        return "id: %s name: %s" % (self.id, self.name)

    class Meta:
        db_table = "video"
        verbose_name = _("VideoModel")
        verbose_name_plural = _("VideoModels")
        ordering = ["position"]
        unique_together = [
            ("content", "position"),
        ]
