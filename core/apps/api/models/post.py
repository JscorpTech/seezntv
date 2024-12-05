from django.db import models
from django.utils.translation import gettext_lazy as _

from core.http.models import AbstractBaseModel


class PostModel(AbstractBaseModel):
    title = models.CharField(verbose_name=_("title"), max_length=255)
    desc = models.TextField(verbose_name=_("desc"))

    def __str__(self):
        return self.title

    class Meta:
        db_table = "post"
        verbose_name = _("PostModel")
        verbose_name_plural = _("PostModels")
