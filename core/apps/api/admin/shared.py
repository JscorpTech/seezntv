from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin
from unfold.forms import ActionForm

from ..models import CadrModel, CategoryModel, CommentModel, GenreModel, IntervalModel, TagModel


@admin.register(CategoryModel)
class CategoryAdmin(SortableAdminMixin, ModelAdmin, TabbedTranslationAdmin):
    action_form = ActionForm
    list_display = ("id", "__str__", "position")
    ordering = ["position"]
    search_fields = ("name",)
    readonly_fields = ["position"]


@admin.register(GenreModel)
class GenreAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = (
        "id",
        "__str__",
    )
    search_fields = ("name",)


@admin.register(CadrModel)
class CadrAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
    search_fields = ("image",)


@admin.register(TagModel)
class TagAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = (
        "id",
        "__str__",
    )
    search_fields = ("name",)


@admin.register(IntervalModel)
class IntervalAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
    search_fields = ("items__video",)


@admin.register(CommentModel)
class CommentAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
