from click_up.views import ClickWebhook
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django_core.mixins import BaseViewSetMixin
from ..serializers import ManualConfirmSerializer
from rest_framework.permissions import AllowAny


class ClickWebhookAPIView(ClickWebhook):
    def successfully_payment(self, params):
        """
        successfully payment method process you can ovveride it
        """
        print(f"payment successful params: {params}")

    def cancelled_payment(self, params):
        """
        cancelled payment method process you can ovveride it
        """
        print(f"payment cancelled params: {params}")


class ManualPaymentView(BaseViewSetMixin, GenericViewSet):
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        match self.action:
            case "confirm":
                return ManualConfirmSerializer
            case _:
                return ManualConfirmSerializer

    @action(methods=["POST"], detail=True, url_name="confirm", url_path="confirm")
    def confirm(self, request, pk):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        return Response({
            "detail": "Slaom bratishka"
        })
