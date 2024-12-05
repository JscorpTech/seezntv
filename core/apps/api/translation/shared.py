from modeltranslation.translator import TranslationOptions, register

from ..models import CategoryModel, GenreModel, TagModel


@register(CategoryModel)
class CategoryTranslation(TranslationOptions):
    fields = []


@register(GenreModel)
class GenreTranslation(TranslationOptions):
    fields = []


@register(TagModel)
class TagTranslation(TranslationOptions):
    fields = []
