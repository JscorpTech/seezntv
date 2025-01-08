from modeltranslation.translator import TranslationOptions, register

from ..models import PlanModel


@register(PlanModel)
class PlanTranslation(TranslationOptions):
    fields = []
