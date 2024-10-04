from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    # images = forms.ImageField(widget=forms.widgets.FileInput(attrs={"multiple": True}))

    class Meta:
        model = Post
        fields = [
            "title",
            "text",
            "is_published",
        ]
