import reflex as rx

from webpage.styles.colors import Color
from webpage.styles.styles import Size, navbar_title_style


def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.text(
                "Seraph",
                style=navbar_title_style
            ),
        ),

        position = "sticky",
        bg=Color.CONTENT.value,
        padding_x= Size.BIG.value,
        padding_y= Size.DEFAULT.value,
        z_index= "999",
        top="0"
    )