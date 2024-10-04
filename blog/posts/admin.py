from django.contrib import admin
from django.forms import ModelForm
from django.http import HttpRequest

from .forms import PostForm
from .models import Image, Post


class ImageInline(admin.StackedInline):
    model = Image
    extra = 1


class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "created_at",
        "author",
    ]
    inlines = [
        ImageInline,
    ]
    form = PostForm

    def save_model(
        self, request: HttpRequest, obj: Post, form: ModelForm, change: bool
    ) -> None:
        if not change:
            obj.author = request.user
        return super().save_model(request, obj, form, change)


admin.site.register(Post, PostAdmin)
