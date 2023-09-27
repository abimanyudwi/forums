from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Translasi, Post, TranslationNote
from django import forms

# from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE

# from main.models import Author
from django.contrib.admin.decorators import display
from django.template.loader import get_template


class TranslasiForms(forms.ModelForm):
    content = forms.CharField(
        required=True, widget=TinyMCE(attrs={"cols": 10, "rows": 10})
    )

    class Meta:
        model = Translasi
        fields = ("content",)


class NoteForms(forms.ModelForm):
    content = forms.CharField(
        required=True,
        widget=TinyMCE(
            attrs={
                "cols": 10,
                "rows": 10,
                "placeholder": "",
                "initValue": "",
                "id": "notecontent",
            }
        ),
    )

    class Meta:
        model = TranslationNote
        fields = ("content",)


# class AnnounceForms(forms.ModelForm):
#     konten = forms.CharField(
#         required=True,
#         widget=TinyMCE(
#             attrs={"cols": 10, "rows": 10, "placeholder": "", "initValue": ""}
#         ),
#     )

#     class Meta:
#         model = Post
#         fields = ("konten",)


class AnnounceForms(forms.ModelForm):
    konten = forms.CharField(
        required=True,
        widget=TinyMCE(
            attrs={"cols": 10, "rows": 10, "placeholder": "", "initValue": ""}
        ),
    )

    class Meta:
        model = Post
        fields = ("konten",)


class PengumumanForms(forms.ModelForm):
    konten = forms.CharField(
        required=True, widget=TinyMCE(attrs={"cols": 10, "rows": 10})
    )

    class Meta:
        model = Post
        fields = ("konten",)
