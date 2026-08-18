"""URL configuration for projects app."""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"projects", views.ProjectViewSet, basename="project")
router.register(r"project-shares", views.ProjectShareViewSet, basename="projectshare")

urlpatterns = [
    path("", include(router.urls)),
]
