"""Welcome to Reflex! This file outlines the steps to create a basic app."""


import reflex as rx

import  webpage.styles.styles as styles
from webpage.pages.index import index
from webpage.pages.presentaciones import presentaciones

class State(rx.State):
    """State for the app."""
    title: str = "Seraph"
    description: str = "Seraph"
    image: str = "/icons/code.svg"
    meta: dict = {
        "name": "Seraph",
        "content": "Seraph",
    }

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
)


