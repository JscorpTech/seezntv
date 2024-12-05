from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import (CadrModel, CategoryModel, GenreModel, IntervalModel,
                      TagModel)


@admin.register(CategoryModel)
class CategoryAdmin(ModelAdmin):
    list_display = ("__str__",)
    search_fields = ("name",)


@admin.register(GenreModel)
class GenreAdmin(ModelAdmin):
    list_display = ("__str__",)
    search_fields = ("name",)


@admin.register(CadrModel)
class CadrAdmin(ModelAdmin):
    list_display = ("__str__",)
    search_fields = ("image",)


@admin.register(TagModel)
class TagAdmin(ModelAdmin):
    list_display = ("__str__",)
    search_fields = ("name",)


@admin.register(IntervalModel)
class IntervalAdmin(ModelAdmin):
    list_display = ("__str__",)
    search_fields = ("items__video",)
