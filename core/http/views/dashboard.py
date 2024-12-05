from django.utils.translation import gettext as _
from core.apps.api import models
from ..models import User


def dashboard_callback(request, context):
    data = {
        "films": models.ContentModel.objects.count(),
        "categories": models.CategoryModel.objects.count(),
        "tags": models.TagModel.objects.count(),
        "genres": models.GenreModel.objects.count(),
        "contents": models.ContentModel.objects.count(),
        "users": User.objects.count(),
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
                    "value": data['categories'],
                    "title": _("categories"),
                },
                {
                    "color": "orange",
                    "value": data['tags'],
                    "title": _("tags"),
                },
                {
                    "color": "red",
                    "value": data['genres'],
                    "title": _("genres"),
                },
                {
                    "color": "green",
                    "value": data['contents'],
                    "title": _("contents"),
                },
                {
                    "color": "red",
                    "value": data['users'],
                    "title": _("users"),
                },
                {
                    "color": "green",
                    "value": data['banners'],
                    "title": _("banners"),
                },
                {
                    "color": "green",
                    "value": data['stories'],
                    "title": _("stories"),
                },
            ),
        }
    )

    return context
