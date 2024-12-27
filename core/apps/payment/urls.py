from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlanView, ClickWebhookAPIView, OrderView

router = DefaultRouter()
router.register("plan", PlanView, "plan")
router.register("order", OrderView, "order")

urlpatterns = [
    path("", include(router.urls)),
    path("click/webhook/", ClickWebhookAPIView.as_view()),
]
