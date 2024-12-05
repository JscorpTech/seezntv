from typing import Any

from django.db.models.query import QuerySet
from django.utils.translation import gettext_lazy as _
from unfold.contrib.filters.admin import DropdownFilter


class CategoryFilter(DropdownFilter):
    title = _("Default name")
    parameter_name = "key"

    def lookups(self, request: Any, model_admin: Any) -> list[tuple[Any, str]]:
        return [("key", _("Select field"))]

    def queryset(self, request: Any, queryset: QuerySet[Any]) -> QuerySet[Any] | None:

        return queryset
