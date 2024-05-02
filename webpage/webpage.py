"""Welcome to Reflex! This file outlines the steps to create a basic app."""


import reflex as rx

from webpage.components.footer import footer
from webpage.components.navbar import navbar
from webpage.views.header import header
from webpage.views.links import links
import  webpage.styles.styles as styles
from webpage.styles.styles import Size

# class State(rx.State):
#     pass


def index() -> rx.Component:
    return rx.box(
        navbar(),

        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.DEFAULT.value,
                padding=Size.MEDIUM.value,
                align="center",
                justify="center"
            ),

            align="center",
            justify="center"
        ),
        rx.center(
            footer(),
            align="center",
            justify="center"
        )
    )


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
)
title = "Seraph page"
app.add_page(
    index,
    title=title,
    description="Bienvenido a la página de Seraph!",
    image="favicon.ico",
    meta=[
        {"name": "og:type", "content": "website"},
        {"name": "og:title", "content": title},
        {"name": "og:description", "content": "Bienvenido a la página de Seraph!"},
    ]
)

