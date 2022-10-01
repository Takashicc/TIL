from django.db import models
from django.utils import timezone


class Article(models.Model):
    title = models.CharField("Title", max_length=100)
    content = models.TextField("Content")
    created_at = models.DateTimeField("Datetime", default=timezone.now)

    def __str__(self) -> str:
        return self.title
