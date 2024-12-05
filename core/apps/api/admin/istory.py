from django.contrib import admin
from unfold.admin import ModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin

from ..models import IstoryModel, IstoryVideoModel


@admin.register(IstoryModel)
class IstoryAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = (
        "id",
        "__str__",
        "created_at",
        "updated_at",
    )
    autocomplete_fields = ("videos",)


@admin.register(IstoryVideoModel)
class IstoryvideoAdmin(ModelAdmin):
    list_display = ("id", "__str__",)
    search_fields = ("video",)
