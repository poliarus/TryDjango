from django.shortcuts import render, get_object_or_404
from .models import Article


def article_list_views(request):
    article_list = Article.objects.all()
    context = {
        "article_list": article_list
    }
    return render(request, "articles/article_list.html", context)


def article_detail_views(request, id):
    article = get_object_or_404(Article, id=id)
    context = {
        "article": article
    }
    return render(request, "articles/article_detail.html", context)
