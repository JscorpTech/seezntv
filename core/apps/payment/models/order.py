from django.db import models
from django_core.models import AbstractBaseModel
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from ..choices import PaymentTypeChoice


class OrderModel(AbstractBaseModel):
    amount = models.BigIntegerField(_("amount"))
    status = models.BooleanField(_("status"), default=False)
    plan = models.ForeignKey(verbose_name=_("plane"), to="PlanModel", null=True, blank=False, on_delete=models.SET_NULL)
    user = models.ForeignKey(verbose_name=_("user"), to=get_user_model(), on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    payment_method = models.CharField(
        _("payemnt method"),
        choices=PaymentTypeChoice.choices,
        default=PaymentTypeChoice.CLICK,
    )
