import reflex as rx

from webpage.styles.colors import Color
from webpage.styles.styles import Size, navbar_title_style
from webpage.views.routes import Route
from webpage.components.ant_components import float_button

def navbar() -> rx.Component:
    return rx.hstack(

        rx.link(
            rx.box(
                rx.text(
                    "Seraph",
                    style=navbar_title_style
                ),
            ),
            href=Route.INDEX.value,
        ),
        float_button(),
        position = "sticky",
        bg=Color.CONTENT.value,
        padding_x= Size.BIG.value,
        padding_y= Size.TINY.value,
        z_index= "999",
        top="0"
    )