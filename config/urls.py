from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from app.views import AiViewSet, FavoriteViewSet, FunctionViewSet, HistoricViewSet
from usuario.router import router as usuario_router
router = DefaultRouter()

router.register(r"ais", AiViewSet)
router.register(r"favorites", FavoriteViewSet)
router.register(r"functions", FunctionViewSet)
router.register(r"historics", HistoricViewSet)

from src.search import search

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api/", include(usuario_router.urls)),
    path("ai/", search, name="ai"),
]
