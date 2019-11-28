from django.urls import path
from .views import *

urlpatterns = [
    path('', article_list_views, name="article-list"),
    path('<int:id>/', article_detail_views, name="article-detail"),
]
