from django.db import models


class VideoContent(models.Model):
    sources = models.URLField()
    skip_start_time = models.DurationField(null=True, blank=True)
    skip_end_time = models.DurationField(null=True, blank=True)

    index = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self) -> str:
        return self.sources.split("/")[-1]
