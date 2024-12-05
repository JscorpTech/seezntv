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


class GenreAdmin(ModelAdmin):
    list_display = ("__str__",)
    search_fields = ("genre__item",)


class CategoryAdmin(ModelAdmin):
    search_fields = ("category__item",)
    list_display = ("__str__",)


class VideoContentAdmin(ModelAdmin):
    search_fields = ("sources",)
    list_display = ("__str__",)


class TagsAdmin(ModelAdmin):
    list_display = ("__str__",)
    search_fields = ("tag",)


class ContentAdmin(ModelAdmin):
    list_display = ("__str__",)
    autocomplete_fields = ("kadrs", "genre", "category", "contents", "ova", "chronology", "tags")


admin.site.register(Content, ContentAdmin)
admin.site.register(VideoContent, VideoContentAdmin)

admin.site.register(Cadr, CadrAdmin)
admin.site.register(GenreItem, ModelAdmin)
admin.site.register(GenreList, GenreAdmin)
admin.site.register(CategoryItem, ModelAdmin)
admin.site.register(CategoryList, CategoryAdmin)
admin.site.register(Tag, TagsAdmin)
admin.site.register(IstoryVideo, ModelAdmin)
admin.site.register(Istory, ModelAdmin)
