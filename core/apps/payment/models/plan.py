from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class PlanModel(AbstractBaseModel):
    name = models.CharField(_("name"), max_length=255)
    price = models.BigIntegerField(_("price"))

    def __str__(self):
        return self.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
            price=10000,
        )

    class Meta:
        db_table = "plan"
        verbose_name = _("PlanModel")
        verbose_name_plural = _("PlanModels")
