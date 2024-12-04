from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import ContentModel


@admin.register(ContentModel)
class ContentAdmin(ModelAdmin):
    list_display = ("__str__",)
    autocomplete_fields = (
        "genre",
        "ova",
        "chronology",
        "tags",
        "cadrs",
        "category",
        "contents",
    )
