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
        "title": _("Dashboard"),
        "separator": True,  # Top border
        "items": [
            {"title": _("Filmlar"), "icon": "videocam", "link": reverse_lazy("admin:api_contentmodel_changelist")},
            {"title": _("Kategoriler"), "icon": "category", "link": reverse_lazy("admin:api_categorymodel_changelist")},
            {"title": _("Janrlar"), "icon": "genres", "link": reverse_lazy("admin:api_genremodel_changelist")},
            {"title": _("Istory"), "icon": "play_circle", "link": reverse_lazy("admin:api_istorymodel_changelist")},
            {"title": _("Taglar"), "icon": "tag", "link": reverse_lazy("admin:api_tagmodel_changelist")},
            {
                "title": _("tarafusslar"),
                "icon": "insert_page_break",
                "link": reverse_lazy("admin:api_intervalmodel_changelist"),
            },
            {
                "title": _("Banner"),
                "icon": "planner_banner_ad_pt",
                "link": reverse_lazy("admin:api_bannermodel_changelist"),
            },
        ],
    },
    {
        "title": _("Auth"),
        "separator": True,  # Top border
        "items": [
            {
                "title": _("Users"),
                "icon": "group",
                "link": reverse_lazy("admin:accounts_user_changelist"),
            },
            {
                "title": _("Group"),
                "icon": "group",
                "link": reverse_lazy("admin:auth_group_changelist"),
            },
        ],
    },
]
