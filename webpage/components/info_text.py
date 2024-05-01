import reflex as rx

from webpage.styles.colors import TextColor, Color
from webpage.styles.styles import Size


def info_text(title: str, body: str) -> rx.Component:
    return rx.hstack(
        rx.text(
            title,
            font_weight="bold",
            color=Color.PRIMARY.value,
        ),
        rx.text(
            body,
            font_size=Size.MEDIUM.value,
            color=TextColor.BODY.value,
        ),
        rx.spacer(),
    )