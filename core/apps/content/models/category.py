from django.db import models


class CategoryItem(models.Model):
    item = models.CharField(max_length=250, unique=True)

    def __str__(self) -> str:
        return self.item


class CategoryList(models.Model):
    category = models.OneToOneField(CategoryItem, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.category)
