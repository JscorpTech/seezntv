from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

PAGES = [
    {
        "seperator": False,
        "items": [
            {
                "title": _("Home page"),
                "icon": "home",
                "link": reverse_lazy("admin:index"),
            }
        ],
    },
    {
        "title": _("Auth"),
        "separator": True,  # Top border
        "items": [
            {
                "title": _("Users"),
                "icon": "group",
                "link": reverse_lazy("admin:http_user_changelist"),
            },
            {
                "title": _("Group"),
                "icon": "group",
                "link": reverse_lazy("admin:auth_group_changelist"),
            },
        ],
    },
    {
        "title": _("Base"),
        "separator": True,  # Top border
        "items": [
            {"title": _("Filmlar"), "icon": "list", "link": reverse_lazy("admin:api_contentmodel_changelist")},
            {"title": _("Kategoriler"), "icon": "list", "link": reverse_lazy("admin:api_categorymodel_changelist")},
            {"title": _("Janrlar"), "icon": "list", "link": reverse_lazy("admin:api_genremodel_changelist")},
            {"title": _("tarafusslar"), "icon": "list", "link": reverse_lazy("admin:api_intervalmodel_changelist")},
            {"title": _("Istory"), "icon": "list", "link": reverse_lazy("admin:api_istorymodel_changelist")},
            {"title": _("Taglar"), "icon": "list", "link": reverse_lazy("admin:api_tagmodel_changelist")},
        ],
    },
]
