from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class PaymentTypeChoice(TextChoices):
    CLICK = "click", _("click")
    PAYNET = "paynet", _("payment")
    PAYME = "payme", _("payme")
