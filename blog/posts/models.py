from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField("titel", max_length=50)
    text = models.TextField()
    number_of_likes = models.IntegerField("antal som gillar", default=0)
    created_at = models.DateTimeField("skapad", auto_now_add=True)
    is_published = models.BooleanField("publicerad", default=False)
    author = models.ForeignKey(
        User, verbose_name="författare", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "inlägg"
        verbose_name_plural = "inlägg"

    def __str__(self) -> str:
        return self.title


class Image(models.Model):
    caption = models.CharField("text", max_length=70)
    file = models.ImageField("fil")
    order = models.PositiveSmallIntegerField("ordning", default=1)
    post = models.ForeignKey(Post, related_name="images", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "bild"
        verbose_name_plural = "bilder"
        ordering = ["order"]

    def __str__(self) -> str:
        return f"#{self.order}"


class Comment(models.Model):
    text = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    author_name = models.CharField(max_length=50)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "kommentar"
        verbose_name_plural = "kommentarer"

    def __str__(self) -> str:
        return f'{self.author_name} commented on "{self.post.title}" @ {self.created_at.isoformat()}'
