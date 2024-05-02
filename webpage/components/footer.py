import reflex as rx
from datetime import datetime

from webpage.constants import PAGINA_URL, REPO_URL
from webpage.styles.colors import TextColor
from webpage.styles.styles import Size

now = datetime.now()
year = now.year


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="favicon.ico",
            height=Size.VERY_BIG.value,
            width=Size.VERY_BIG.value,
            alt="Favico analista",
        ),
        rx.link(
            f"\u00A9 2008-{year} Seraph by Ernesto Crespo  V5",
            href=PAGINA_URL,
            is_external=True,
            font_size=Size.MEDIUM.value
        ),
        rx.hstack(
            rx.link(
                rx.image(
                    src="icons/github.svg",
                    height=Size.LARGE.value,
                    width=Size.LARGE.value,
                ),
                href=REPO_URL,
                is_external=True
            ),
            rx.text(
                "Developing software with Python and Linux",
                font_size=Size.MEDIUM.value,
                margin_top=Size.ZERO.value,
            ),
        ),
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        padding_x=Size.BIG.value,
        color=TextColor.BODY.value,
        align="center",
        justify="center"
    )