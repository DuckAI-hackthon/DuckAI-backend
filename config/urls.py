from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from usuario.router import router as usuario_router
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from django.conf import settings
from django.conf.urls.static import static
from uploader.router import router as uploader_router
from src.search import search
from usuario import cadastro

from app.views import AiViewSet, FavoriteViewSet, FunctionViewSet, HistoricViewSet, ChatViewSet, ChatHistoryViewSet

router = DefaultRouter()
router.register(r"ais", AiViewSet)
router.register(r"favorites", FavoriteViewSet)
router.register(r"functions", FunctionViewSet)
router.register(r"historics", HistoricViewSet)
router.register(r"chats", ChatViewSet)
router.register(r"chatHistories", ChatHistoryViewSet)



urlpatterns = [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("api/", include(usuario_router.urls)),
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("ai/", search, name="ai"),
    path("api/media/", include(uploader_router.urls)),    
    path('api/signup/', cadastro.create_user, name='create_user'),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
