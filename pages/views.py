from django.shortcuts import render


def home_view(request):
    return render(request, "home.html", {})


def about_view(request):
    my_context = {
        "my_text": "This is about me",
        "this_is_true": True,
        "my_list": [123, 456, 789, "abc", [1, 2, 3, 4, 5]],
        "my_html": "<h4>Hello world</h4>"       # {{ my_html|safe }}
    }
    return render(request, "about.html", my_context)


def contact_view(request):
    return render(request, "contact.html", {})


def product_view(request):
    return render(request, "product.html", {})
