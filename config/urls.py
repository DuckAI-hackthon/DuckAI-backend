from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from app.views import AiViewSet, FavoriteViewSet, FunctionViewSet, HistoricViewSet, ChatViewSet, ChatHistoryViewSet

router = DefaultRouter()

router.register(r"ais", AiViewSet)
router.register(r"favorites", FavoriteViewSet)
router.register(r"functions", FunctionViewSet)
router.register(r"historics", HistoricViewSet)
router.register(r"chats", ChatViewSet)
router.register(r"chatHistories", ChatHistoryViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
