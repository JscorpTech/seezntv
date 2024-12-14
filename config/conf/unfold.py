from . import navigation

from django.utils.translation import gettext as _
from core.apps.api import models
from django.contrib.auth import get_user_model

UNFOLD = {
    "DASHBOARD_CALLBACK": "config.conf.dashboard_callback",
    "SITE_TITLE": None,
    "SHOW_LANGUAGES": True,
    "SITE_HEADER": None,
    "SITE_URL": "/",
    "SITE_SYMBOL": "speed",  # symbol from icon set
    "SHOW_HISTORY": True,  # show/hide "History" button, default: True
    "SHOW_VIEW_ON_SITE": True,
    "COLORS": {
        "primary": {
            "50": "220 255 230",
            "100": "190 255 200",
            "200": "160 255 170",
            "300": "130 255 140",
            "400": "100 255 110",
            "500": "70 255 80",
            "600": "50 225 70",
            "700": "40 195 60",
            "800": "30 165 50",
            "900": "20 135 40",
            "950": "10 105 30",
        },
    },
    "EXTENSIONS": {
        "modeltranslation": {
            "flags": {
                "en": "🇬🇧",
                "uz": "🇺🇿",
                "ru": "🇷🇺",
            },
        },
    },
    "SIDEBAR": {
        "show_search": True,  # Search in applications and models names
        "show_all_applications": True,
        "navigation": navigation.PAGES,  # Pagelarni qo'lda qo'shish
    },
}


def dashboard_callback(request, context):
    data = {
        "films": models.ContentModel.objects.count(),
        "categories": models.CategoryModel.objects.count(),
        "tags": models.TagModel.objects.count(),
        "genres": models.GenreModel.objects.count(),
        "contents": models.ContentModel.objects.count(),
        "users": get_user_model().objects.count(),
        "banners": models.BannerModel.objects.count(),
        "stories": models.IstoryModel.objects.count(),
    }

    context.update(
        {
            "cards": (
                {
                    "color": "blue",
                    "value": data["films"],
                    "title": _("films"),
                },
                {
                    "color": "primary",
                    "value": data["categories"],
                    "title": _("categories"),
                },
                {
                    "color": "orange",
                    "value": data["tags"],
                    "title": _("tags"),
                },
                {
                    "color": "red",
                    "value": data["genres"],
                    "title": _("genres"),
                },
                {
                    "color": "green",
                    "value": data["contents"],
                    "title": _("contents"),
                },
                {
                    "color": "red",
                    "value": data["users"],
                    "title": _("users"),
                },
                {
                    "color": "green",
                    "value": data["banners"],
                    "title": _("banners"),
                },
                {
                    "color": "green",
                    "value": data["stories"],
                    "title": _("stories"),
                },
            ),
        }
    )

    return context
