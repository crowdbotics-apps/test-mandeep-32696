from django.conf import settings
from django.db import models


class School(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )
    address = models.CharField(
        max_length=256,
    )
    principal_name = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="school_principal_name",
    )
    active = models.BooleanField(
        null=True,
        blank=True,
    )


class ClassMaster(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )
    active = models.BooleanField()
    title = models.CharField(
        max_length=256,
    )
