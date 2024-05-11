import reflex as rx

from webpage.components.footer import footer
from webpage.components.navbar import navbar
from webpage.components.sidebar import sidebar
from webpage.styles.colors import Color
from webpage.views.routes import Route
from webpage.views.presentaciones_links import presentaciones_links
import webpage.styles.styles as styles
from webpage.styles.styles import Size
from webpage import utils



@rx.page(
    route=Route.PRESENTACIONES.value,
    title=utils.PRESENTER_TITLE,
    description=utils.PRESENTER_DESCRIPTION,
    image=utils.PRESENTER_IMAGE,
    meta=utils.presenter_meta
)
def presentaciones() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        sidebar(),

        rx.center(
            rx.vstack(
                presentaciones_links(),
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
        ),
        bg=Color.CONTENT.value,
    )

