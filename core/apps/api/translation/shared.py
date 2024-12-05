from modeltranslation.translator import TranslationOptions, register

from ..models import CategoryModel, GenreModel, TagModel


@register(CategoryModel)
class CategoryTranslation(TranslationOptions):
    fields = [
        "name"
    ]


@register(GenreModel)
class GenreTranslation(TranslationOptions):
    fields = [
        "name"
    ]


@register(TagModel)
class TagTranslation(TranslationOptions):
    fields = [
        "name"
    ]
