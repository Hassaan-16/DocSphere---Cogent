from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"organizations", views.OrganizationViewSet, basename="organization")
router.register(
    r"subscriptions", views.OrganizationSubscriptionViewSet, basename="subscription"
)

urlpatterns = [
    path("", include(router.urls)),
]
