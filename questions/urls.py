from django.urls import path, include
from rest_framework import routers

from questions.api.viewsets import QuestionViewSet, CategoryViewSet


categories_router = routers.DefaultRouter()
categories_router.register(
    prefix="",
    viewset=CategoryViewSet,
    basename="categories",
)

questions_router = routers.DefaultRouter()
questions_router.register(
    prefix="",
    viewset=QuestionViewSet,
    basename="questions",
)


urlpatterns = [
    path("questions", include(questions_router.urls), name='questions'),
    path("categoires", include(categories_router.urls), name='categories'),
]

