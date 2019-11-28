from django import forms
from .models import CBV


class CBVModelForm(forms.ModelForm):
    class Meta:
        model = CBV
        fields = [
            "title",
            "content",
            "active"
        ]

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if title.lower() == "abc":
            raise forms.ValidationError("This is not a valid title")
        return title
