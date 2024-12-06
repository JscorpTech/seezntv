from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline, StackedInline
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.contrib.filters.admin import MultipleRelatedDropdownFilter
from ..models import ContentModel, VideoModel, CadrModel


class VideoInline(TabularInline):
    model = VideoModel
    extra = 1
    tab = True


class CadrInline(StackedInline):
    model = CadrModel
    extra = 1
    tab = True


@admin.register(ContentModel)
class ContentAdmin(ModelAdmin, TabbedTranslationAdmin):
    inlines = [VideoInline, CadrInline]
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
        "category",
    )
