from rest_framework.viewsets import GenericViewSet
from django_core.mixins import BaseViewSetMixin
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from ..serializers import CreateOrderSerializer, ListOrderSerializer
from ..services import PaymentService


class OrderView(BaseViewSetMixin, GenericViewSet):
    def get_serializer_class(self):
        match self.action:
            case "create":
                return CreateOrderSerializer
            case _:
                return ListOrderSerializer

    def get_permissions(self):
        perms = []
        match self.action:
            case "create":
                perms.extend([IsAuthenticated])
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save(user=request.user)
        data = serializer.validated_data
        service = PaymentService()
        return Response(
            {
                "detail": "Order yaratildi",
                "order_id": order.id,
                "payment_url": service.generate_link(
                    order.id, order.amount, data.get("payment_type", data.get("payment_method"))
                ),
            }
        )
