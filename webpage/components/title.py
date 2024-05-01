import reflex as rx

from webpage.styles import styles


def title(text: str) -> rx.Component:
    return rx.heading(
        text,
        size="5",
        style=styles.title_style
    )
