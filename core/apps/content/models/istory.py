from django.db import models

from core.apps.content.models.content import Content


class IstoryVideo(models.Model):
    video = models.URLField()

    def __str__(self) -> str:
        return self.video.split("/")[-1]


class Istory(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    videos = models.ManyToManyField(IstoryVideo)

    def __str__(self) -> str:
        return str(self.content)
