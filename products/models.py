from django.db import models
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summery = models.TextField(blank=True, null=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return f"/products/{self.id}"
        return reverse("product-id", kwargs={"id": self.id})
