from enum import Enum

import reflex as rx
from webpage.styles.colors import Color, TextColor
from webpage.styles.fonts import Font, FontWeight

# Constants
MAX_WIDTH = "600px"

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap",
    "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css",
]


# Sizes
class Size(Enum):
    ZERO = "0px !important"
    TINY = "0.2em"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "3em"



BASE_STYLE = {
    "background_color": Color.BACKGROUND.value,
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    rx.heading: {
        "color": TextColor.HEADER.value,
        "font_family":Font.TITLE.value,
        "font_weight": FontWeight.MEDIUM.value,
    },
    rx.button: {
        "width": "100%",
        "height": "100%",
        # "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": TextColor.HEADER.value,
        "background_color": Color.CONTENT.value,
        "white_space": "normal",
        "text_align": "start",
        "_hover": {
            "background_color": Color.SECONDARY.value,
        },
    },
    rx.link: {
        "text_decoration":"none",
        "_hover": {}
    }
}

navbar_title_style = dict(
    font_family=Font.LOGO.value,
    font_weight=FontWeight.MEDIUM.value,
    color=Color.PRIMARY.value,
    font_size=Size.LARGE.value,
)

title_style = dict(
    width="100%",
    font_family=Font.TITLE.value,
    font_weight=FontWeight.MEDIUM.value,
    padding_top=Size.DEFAULT.value,
    color=TextColor.HEADER.value,
)

button_title_style = dict(
    font_size=Size.DEFAULT.value,
    font_family=Font.TITLE.value,
    font_weight=FontWeight.LIGHT.value,
    color=TextColor.HEADER.value,
)

button_body_style = dict(
    font_size=Size.MEDIUM.value,
    font_family=Font.DEFAULT.value,
    color=TextColor.BODY.value,
)