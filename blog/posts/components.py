from collections.abc import Iterable
from pathlib import Path

import htpy as h
from django.conf import settings
from django.templatetags.static import static
from markupsafe import Markup
from zoneinfo import ZoneInfo

from .models import Image, Post

PAGE_TITLE = "6 veckor i Vietnam"


def image(image: Image) -> h.Node:
    url = str(Path(settings.MEDIA_URL) / image.file.name)
    return h.article[
        h.a(href=str(Path(settings.MEDIA_URL) / image.file.name))[h.img(src=url)],
        h.p[image.caption],
    ]


def post(post: Post) -> h.Node:
    def format_created_at(timezone_identifier: str) -> str:
        return post.created_at.astimezone(ZoneInfo(timezone_identifier)).isoformat(
            sep=" ", timespec="minutes"
        )

    paragraphs = [h.p[line] for line in post.text.splitlines()]
    return h.article[
        h.section[h.h2[post.title.title()]],
        h.section[paragraphs],
        h.section(".grid")[(image(i) for i in post.images.all())],
        h.section[
            h.article[format_created_at("Europe/Stockholm")],
            h.article[f"Skrivet av {post.author.username.title()}"],
            h.article[format_created_at("Asia/Ho_Chi_Minh")],
        ],
        h.hr,
    ]


def time_is() -> Markup:
    return Markup(
        """
        <a href="https://time.is/Vietnam" id="time_is_link" rel="nofollow" target="_blank">Lokal tid i Vietnam:</a>
        <span class="widget" id="Vietnam_z418"></span>
        <script src="//widget.time.is/sv.js"></script>
        <script>
        time_is_widget.init({Vietnam_z418:{template:"DATE<br>TIME<br>SUN", date_format:"dayname dnum monthname year", sun_format:"Soluppgång: srhour:srminute Solnedgång: sshour:ssminute", coords:"16.1666700,107.8333300"}});
        </script>
        """
    )


def feed(posts: Iterable[Post]) -> h.Node:
    return h.html(lang="sv", charset="utf-8")[
        h.title[PAGE_TITLE],
        h.link(rel="icon", type="image/x-icon", href=static("flag_vn.svg")),
        h.link(rel="preconnect", href="https://fonts.googleapis.com"),
        h.link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=True),
        h.link(
            href="https://fonts.googleapis.com/css2?family=KoHo:ital,wght@0,400;0,700;1,400;1,700&display=swap",
            rel="stylesheet",
        ),
        h.link(
            rel="stylesheet",
            href=static("styles.css"),
        ),
        h.main[
            h.header[
                h.h1[PAGE_TITLE],
                h.p[
                    """
                    Kul att du har hittat hit!
                    Vi (David och Tobias) spenderar 6 veckor i Vietnam och mestadels trampandes på våra cyklar.
                    Resan börjar 5:e oktober med flyg och vi börjar trampa 6:e oktober.
                    Följ oss på vår resa här!
                    """
                ],
            ],
            h.hr,
            h.section[(post(p) for p in posts)],
            h.footer[time_is()],
        ],
    ]
