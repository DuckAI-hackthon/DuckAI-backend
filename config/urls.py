from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from app.views import TranslationViewSet

router = DefaultRouter()
router.register(r"translations", TranslationViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
