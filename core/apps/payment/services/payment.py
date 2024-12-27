from click_up import ClickUp
from config.env import env


class PaymentService:

    def __init__(self): ...

    def generate_link(self, order: int, amount: int, service: str) -> str:
        match service:
            case "click":
                return self._generate_click_link(order, amount)
            case _:
                raise Exception("Service not supported")

    def _generate_click_link(self, order: int, amount: int) -> str:
        clickup = ClickUp(env.str("CLICK_SERVICE_ID"), env.str("CLICK_MERCHANT_ID"))
        return clickup.initializer.generate_pay_link(
            order,
            amount,
            env.str("CLICK_REDIRECT_URL"),
        )
