from modeltranslation.translator import TranslationOptions, register

from ..models import BannerModel


@register(BannerModel)
class BannerTranslation(TranslationOptions):
    fields = ["content"]
