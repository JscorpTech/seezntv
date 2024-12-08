from django.contrib import admin
from unfold.admin import ModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin

from ..models import IstoryModel, IstoryVideoModel
from unfold.forms import ActionForm
from adminsortable2.admin import SortableAdminMixin


@admin.register(IstoryModel)
class IstoryAdmin(SortableAdminMixin, ModelAdmin, TabbedTranslationAdmin):
    action_form = ActionForm
    ordering = ["position"]
    readonly_fields = ["position"]
    list_display = ("id", "__str__", "created_at", "updated_at", "position")
    autocomplete_fields = ("videos",)


@admin.register(IstoryVideoModel)
class IstoryvideoAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
    search_fields = ("video",)
