from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self) -> str:
        return str(self.name)
