# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ActivityViewSet, DayWiseActivityViewSet

router = DefaultRouter()
router.register(r"categories", CategoryViewSet)
router.register(r"activities", ActivityViewSet)
router.register(r"daywise-activities", DayWiseActivityViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
