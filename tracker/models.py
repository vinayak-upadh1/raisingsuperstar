from django.db import models
from django.contrib.auth.models import User


# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# Activity Model
class Activity(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="activities"
    )
    name = models.CharField(max_length=200)
    frequency = models.CharField(max_length=50)  # Example: "2x/Day", "3x/Week"
    duration = models.IntegerField(help_text="Duration in seconds")

    def __str__(self):
        return self.name


# Day-Wise Activity Tracking
class DayWiseActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    date = models.DateField()
    completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ("user", "activity", "date")

    def __str__(self):
        return f"{self.user.username} - {self.activity.name} - {self.date} - {'Completed' if self.completed else 'Pending'}"
