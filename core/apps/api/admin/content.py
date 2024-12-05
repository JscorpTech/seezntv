from django.contrib import admin
from unfold.admin import ModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin

from ..models import ContentModel


@admin.register(ContentModel)
class ContentAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = (
        "id",
        "__str__",
        "created_at",
        "updated_at",
    )
    search_fields = (
        "description",
        "title",
    )
    autocomplete_fields = (
        "genre",
        "ova",
        "chronology",
        "tags",
        "cadrs",
        "category",
        "contents",
    )
