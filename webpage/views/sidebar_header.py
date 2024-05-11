import reflex as rx

from webpage.components.info_text import info_text
from webpage.components.link_icon import link_icon
from webpage.constants import TWITTER_URL, LINKEDIN_URL, PAGINA_URL, MEDIUM_URL, GITHUB_URL
from webpage.styles.colors import TextColor, Color
from webpage.styles.fonts import Font
from webpage.styles.styles import Size


def sidebar_header()-> rx.Component:
    return rx.vstack(
        rx.hstack(
        rx.avatar(
            fallback="EC",
            src="/img.png",
            alt="Avatar de Ernesto Crespo",
            variant="soft",
            color_scheme="crimson",
            high_contrast=True,
            bg=Color.CONTENT.value,
            color=TextColor.BODY.value,
            radius="full",
            size="8",
            padding="2px",

            border_width="4px",
            border_color=Color.PRIMARY.value,
            ),
            rx.vstack(
                rx.heading(
                    "Ernesto Crespo",
                ),
                rx.text(
                    "@seraph13_",
                    size="3",
                    margin_top=Size.ZERO.value,
                    color=TextColor.BODY.value,
                ),
                rx.hstack(

                    link_icon("/icons/github.svg",GITHUB_URL,"Enlace de github"),
                    link_icon("/icons/x.svg", TWITTER_URL,"Enlace de twitter"),
                    link_icon("/icons/linkedin.svg", LINKEDIN_URL,"Enlace de linkedin"),
                    spacing="5",
                    width="100%",
                ),
                spacing="5",
                align_items="start",
            ),
        ),
        rx.flex(
            info_text("+23","años de experiencia"),
            rx.spacer(),
            info_text("+25", "años de desarrollando con Python"),
            rx.spacer(),
        ),
        rx.text("""Soy Ingeniero Electricista dedicado a la ingenieria de software, 
                mucho Linux y Python en ciencia de datos",
                Tambien me gusta la musica electronica, series y películas""",
                font_size=Size.MEDIUM.value,
                color=TextColor.BODY.value,
                ),
        spacing="5",
        padding_y="2em",
        align_items="start",
    )