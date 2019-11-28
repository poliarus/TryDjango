from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_article_url(self):
        return reverse("article-detail", kwargs={"id": self.id})

    def get_article_list_url(self):
        return reverse("article-list")
