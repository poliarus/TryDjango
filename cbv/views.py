from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
from .forms import CBVModelForm
from .models import CBV


class CBVCreateView(CreateView):
    template_name = "cbv/cbv_create.html"
    form_class = CBVModelForm
    queryset = CBV.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)

    # def get_success_url(self):
    #     return "/"


class CBVListView(ListView):
    template_name = "cbv/cbv_list.html"
    context_object_name = "cbv_item_list"
    queryset = CBV.objects.all()            # default  -->  <app_name>/<model_name>_list.html


class CBVDetailView(DetailView):
    template_name = "cbv/cbv_detail.html"

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return get_object_or_404(CBV, id=id_)


class CBVUpdateView(UpdateView):
    template_name = "cbv/cbv_update.html"
    form_class = CBVModelForm
    queryset = CBV.objects.all()

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return get_object_or_404(CBV, id=id_)

    def form_valid(self, form):
        return super().form_valid(form)


class CBVDeleteView(DeleteView):
    template_name = "cbv/cbv_delete.html"
    # success_url = "/cbv/"

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return get_object_or_404(CBV, id=id_)

    def get_success_url(self):
        return reverse("cbv:cbv-list")
