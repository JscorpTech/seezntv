from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.content.models import (
    Cadr,
    CategoryItem,
    CategoryList,
    Content,
    GenreItem,
    GenreList,
    Istory,
    IstoryVideo,
    Tag,
    VideoContent,
)


class CadrAdmin(ModelAdmin):
    list_display = ("__str__",)
    search_fields = ("cadr",)


class ContentAdmin(ModelAdmin):
    list_display = ("__str__",)
    autocomplete_fields = (
        "kadrs",
        "genre",
        "category",
        "contents",
        "ova",
        "chronology",
        "tags"
    )


admin.site.register(Content, ContentAdmin)
admin.site.register(VideoContent, ModelAdmin)

admin.site.register(Cadr, ModelAdmin)
admin.site.register(GenreItem, ModelAdmin)
admin.site.register(GenreList, ModelAdmin)
admin.site.register(CategoryItem, ModelAdmin)
admin.site.register(CategoryList, ModelAdmin)
admin.site.register(Tag, ModelAdmin)
admin.site.register(IstoryVideo, ModelAdmin)
admin.site.register(Istory, ModelAdmin)
