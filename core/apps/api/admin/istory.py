from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import IstoryModel, IstoryVideoModel


@admin.register(IstoryModel)
class IstoryAdmin(ModelAdmin):
    list_display = (
        "__str__",
        "created_at",
        "updated_at",
    )
    autocomplete_fields = ("videos",)


@admin.register(IstoryVideoModel)
class IstoryvideoAdmin(ModelAdmin):
    list_display = ("__str__",)
    search_fields = ("video",)
