from django.db import models
from django.urls import reverse


class CBV(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("cbv:cbv-detail", kwargs={"id": self.id})
