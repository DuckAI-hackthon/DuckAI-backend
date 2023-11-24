from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from app.views import TranslationViewSet, ResumeViewSet, KeyWordsViewSet

router = DefaultRouter()

router.register(r"translations", TranslationViewSet)
router.register(r"resumes", ResumeViewSet)
router.register(r"keywords", KeyWordsViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
