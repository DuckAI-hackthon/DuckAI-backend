from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from app.views import AiViewSet, FavoriteViewSet, FunctionViewSet, HistoricViewSet
from app.views import TranslationViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()

router.register(r"ais", AiViewSet)
router.register(r"favorites", FavoriteViewSet)
router.register(r"functions", FunctionViewSet)
router.register(r"historics", HistoricViewSet)

from src.search import search

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    path("ai/", search, name="ai"),
]
