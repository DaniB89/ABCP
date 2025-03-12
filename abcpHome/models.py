# abcpHome/models.py
from django.db import models


class TechDot(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

