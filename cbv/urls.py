from django.urls import path
from cbv.views import *

app_name = "cbv"
urlpatterns = [
    path('', CBVListView.as_view(), name="cbv-list"),
    path('<int:id>/', CBVDetailView.as_view(), name="cbv-detail"),
    path('create/', CBVCreateView.as_view(), name="cbv-create"),
    path('<int:id>/update/', CBVUpdateView.as_view(), name="cbv-update"),
    path('<int:id>/delete/', CBVDeleteView.as_view(), name="cbv-delete"),
]
