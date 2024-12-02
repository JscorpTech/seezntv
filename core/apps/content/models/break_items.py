from django.db import models

from core.apps.content.models.content import Content


class BreaksItem(models.Model):
    break_item = models.ForeignKey(Content, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.break_item.title


class BreakList(models.Model):
    item = models.ManyToManyField(BreaksItem, blank=True)

    def __str__(self) -> str:
        items = self.item.all()

        return ", ".join([str(i.break_item) for i in items])
