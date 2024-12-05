from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import PostModel


@admin.register(PostModel)
class PostAdmin(ModelAdmin):
    list_display = ("__str__",)
