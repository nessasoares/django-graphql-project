from django.db import models
from model_utils.models import TimeStampedModel, UUIDModel


class Todo(TimeStampedModel, UUIDModel, models.Model):
    text = models.TextField()
    completed = models.BooleanField(default=False)
