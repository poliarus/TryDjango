from django.urls import path
from .views import *

urlpatterns = [
    path('', product_list_view, name="product-list"),
    path('create/', product_create_view, name="create"),
    # path('product/', product_detail_view, name="product-detail"),
    path('<int:id>/', dynamic_lookup_view, name="product-id"),
    path('<int:id>/delete', product_delete_view, name="product-delete"),
]
