from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(max_length=50, widget=forms.Textarea(attrs={"rows": 1, "cols": 50}))
    description = forms.CharField(max_length=200, widget=forms.Textarea(attrs={"rows": 20, "cols": 100}))
    summery = forms.CharField(max_length=250, widget=forms.Textarea(attrs={"cols": 100, "row": 20}))

    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "price",
            "summery"
        ]

    # def clean_title(self):
    #     title = self.cleaned_data.get("title")
    #     if "eugene" not in title:
    #         raise forms.ValidationError("This is not a valid title!")
    #     return title


class RawProductForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=200, widget=forms.Textarea(attrs={
        "class": "new-class name one two", "rows": 20, "cols": 100
    }))
    price = forms.DecimalField(initial=0.00, decimal_places=2, max_digits=10000)
    summery = forms.CharField(max_length=250, widget=forms.Textarea(attrs={"cols": 100, "row": 20}))
