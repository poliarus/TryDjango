from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RawProductForm


# def product_create_view(request):
#     form = RawProductForm()
#     if request.method == "POST":
#         form = RawProductForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             Product.objects.create(**form.cleaned_data)
#             form = RawProductForm()
#         else:
#             print(form.errors)
#
#     context = {
#         "form": form
#     }
#
#     return render(request, "products/product_create.html", context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        "form": form
    }

    return render(request, "products/product_create.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     "title": obj.title,
    #     "description": obj.description,
    #     "price": obj.price,
    #     "summery": obj.summery,
    #     "active": obj.active
    # }
    context = {
        "object": obj
    }

    return render(request, "products/product_detail.html", context)


# def render_initial_data(request):
#     initial_data = {
#         "title": "My awesome title"
#     }
#
#     form = RawProductForm(request.POST or None, initial=initial_data)
#     if form.is_valid():
#         form.save()
#     context = {
#         "form": form
#     }
#
#     return render(request, "products/product_create.html", context)


def dynamic_lookup_view(request, id):
    # obj = Product.objects.get(id=id)
    obj = get_object_or_404(Product, id=id)
    # try:
    #     obj = Product.objects.get(id=id)
    # except Product.DoesNotExist:
    #     raise Http404
    context = {
        "object": obj
    }

    return render(request, "products/product_detail.html", context)


def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect("product_detail_view")
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)
