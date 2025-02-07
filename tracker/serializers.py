# serializers.py
from rest_framework import serializers
from .models import Category, Activity, DayWiseActivity


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = "__all__"


class DayWiseActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = DayWiseActivity
        fields = "__all__"
