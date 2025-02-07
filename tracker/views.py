# views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Category, Activity, DayWiseActivity
from .serializers import (
    CategorySerializer,
    ActivitySerializer,
    DayWiseActivitySerializer,
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class DayWiseActivityViewSet(viewsets.ModelViewSet):
    queryset = DayWiseActivity.objects.all()
    serializer_class = DayWiseActivitySerializer
    permission_classes = [IsAuthenticated]
