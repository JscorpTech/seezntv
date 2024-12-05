from modeltranslation.translator import TranslationOptions, register

from ..models import ContentModel


@register(ContentModel)
class ContentTranslation(TranslationOptions):
    fields = [
        "title",
        "description"
    ]
