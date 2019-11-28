from django.db import models
from django.urls import reverse


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=False)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courses:course-detail", kwargs={"id": self.id})
