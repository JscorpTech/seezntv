from django.conf import settings


class FilterService:

    def __init__(self): ...

    @staticmethod
    def get_fields_locale(fields):
        return (*["%s_%s" % (field, language) for language in settings.MODELTRANSLATION_LANGUAGES for field in fields],)
