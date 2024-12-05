from django.db import models


class GenreItem(models.Model):
    item = models.CharField(max_length=250, unique=True)

    def __str__(self) -> str:
        return self.item


class GenreList(models.Model):
    genre = models.OneToOneField(GenreItem, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.genre)
