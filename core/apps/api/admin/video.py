from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import VideoModel


@admin.register(VideoModel)
class VideoAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
