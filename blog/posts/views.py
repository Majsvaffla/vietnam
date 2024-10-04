from django.http import HttpRequest, HttpResponse

from . import components
from .models import Post


def feed(request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        components.feed(Post.objects.filter(is_published=True).order_by("-created_at"))
    )
