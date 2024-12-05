from django.contrib import admin
from unfold.admin import ModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin
from ..models import BannerModel
from adminsortable2.admin import SortableAdminMixin
from unfold.forms import ActionForm


@admin.register(BannerModel)
class BannerAdmin(SortableAdminMixin, ModelAdmin, TabbedTranslationAdmin):
    action_form = ActionForm
    list_display = (
        "id",
        "__str__",
        "film__title",
        "created_at",
        "updated_at",
        "position",
    )
    ordering = ['position']
    autocomplete_fields = [
        "film",
    ]
