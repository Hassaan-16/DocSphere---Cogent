"""URL configuration for documents app."""

from django.urls import include, path

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"documents", views.DocumentViewSet, basename="document")
router.register(
    r"document-shares", views.DocumentShareViewSet, basename="documentshare"
)
urlpatterns = [
    path("", include(router.urls)),
]
