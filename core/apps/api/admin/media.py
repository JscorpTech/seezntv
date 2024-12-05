from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import MediaModel


@admin.register(MediaModel)
class MediaAdmin(ModelAdmin):
    list_display = ("id", "__str__",)
    search_fields = ("video",)
