"""URL configuration for organizations app."""

from django.urls import include, path
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
