from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from app.views import TranslationViewSet, ResumeViewSet, KeyWordsViewSet, QuestionViewSet

router = DefaultRouter()

router.register(r"translations", TranslationViewSet)
router.register(r"resumes", ResumeViewSet)
router.register(r"keywords", KeyWordsViewSet)
router.register(r"questions", QuestionViewSet)

from src.search import search

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),

    path("ai/", search, name="ai"),
]
