from django.db import models
from utils.models import BaseAbstractModel
from utils.managers import CustomQuerySet


class Team(BaseAbstractModel):
    "models for creating a team or organization"
    name = models.CharField(max_length=25)
    description = models.TextField(max_length=255)

    active_objects = CustomQuerySet.as_manager()
    objects = models.Manager()

    def __str__(self):
        return f'{self.name}'
