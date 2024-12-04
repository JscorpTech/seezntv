from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import IstoryModel, IstoryVideoModel


@admin.register(IstoryModel)
class IstoryAdmin(ModelAdmin):
    list_display = ("__str__",)


@admin.register(IstoryVideoModel)
class IstoryvideoAdmin(ModelAdmin):
    list_display = ("__str__",)
