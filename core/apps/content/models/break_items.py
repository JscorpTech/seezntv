from django.db import models

from core.apps.content.models.content import Content


class Break(models.Model):
    content = models.ManyToManyField(Content, blank=True)

    def __str__(self) -> str:

        return ", ".join([str(i) for i in self.content])
