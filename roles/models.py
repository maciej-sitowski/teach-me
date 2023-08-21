from django.conf import settings
from django.db import models

# Create your models here.


class Role(models.Model):
    name = models.CharField(max_length=150)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.name}"
