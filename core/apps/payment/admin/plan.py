from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import PlanModel


@admin.register(PlanModel)
class PlanAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
