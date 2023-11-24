from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from app.views import AiViewSet, FavoriteViewSet, FunctionViewSet, HistoricViewSet

router = DefaultRouter()

router.register(r"ais", AiViewSet)
router.register(r"favorites", FavoriteViewSet)
router.register(r"functions", FunctionViewSet)
router.register(r"historics", HistoricViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
