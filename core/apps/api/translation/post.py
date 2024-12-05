from modeltranslation.translator import TranslationOptions, register

from ..models import PostModel


@register(PostModel)
class PostTranslation(TranslationOptions):
    fields = []
