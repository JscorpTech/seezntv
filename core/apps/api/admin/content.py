from django.contrib import admin
from unfold.admin import ModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.contrib.filters.admin import MultipleRelatedDropdownFilter

from ..models import ContentModel


@admin.register(ContentModel)
class ContentAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_filter = [
        ("category", MultipleRelatedDropdownFilter),
        ("genre", MultipleRelatedDropdownFilter),
        ("tags", MultipleRelatedDropdownFilter),
    ]
    list_filter_submit = True
    list_display = (
        "id",
        "__str__",
        "created_at",
        "updated_at",
    )
    search_fields = (
        "id",
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
