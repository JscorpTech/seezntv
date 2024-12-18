from modeltranslation.translator import TranslationOptions, register

from ..models import IstoryModel


@register(IstoryModel)
class IstoryTranslation(TranslationOptions):
    fields = ["desc"]
