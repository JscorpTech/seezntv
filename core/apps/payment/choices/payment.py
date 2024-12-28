from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class PaymentTypeChoice(TextChoices):
    CLICK = "click", _("click")
    PAYNET = "paynet", _("payment")
    PAYME = "payme", _("payme")
    MANUAL = "manual", _("manual")


class OrderStatusChoice(TextChoices):
    CREATED = "created", _("created")
    PENDING = "pending", _("pending")
    ACTIVE = "active", _("active")
    FINISHED = "finished", _("finished")
