import reflex as rx

from webpage.components.select_presentation import select_presentation
from webpage.styles.colors import Color, TextColor
from webpage.views.sidebar_header import sidebar_header


def sidebar():
    return rx.vstack(

        sidebar_header(),

        position="fixed",
        height="100%",
        left="0px",
        top="0px",
        z_index="5",
        padding_x="2em",
        padding_y="1em",
        # background_color="lightgray",
        align_items="left",
        width="19.5em",
        bg=Color.CONTENT.value,
    )