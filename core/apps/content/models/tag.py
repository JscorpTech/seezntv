from django.db import models


class Tag(models.Model):
    tag = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.tag
