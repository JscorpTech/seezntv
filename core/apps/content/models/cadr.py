from django.db import models


class Cadr(models.Model):
    cadr = models.URLField(unique=True)

    def __str__(self) -> str:
        return self.cadr.split("/")[-1]
