from django.db import models


class Counter(models.Model):
    """Fake counter"""

    name = models.CharField(max_length=100, unique=True)
    value = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
