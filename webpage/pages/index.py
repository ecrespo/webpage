import reflex as rx

from webpage.components.footer import footer
from webpage.components.navbar import navbar
from webpage.views.routes import Route
from webpage.views.header import header
from webpage.views.index_links import index_links
import webpage.styles.styles as styles
from webpage.styles.styles import Size
from webpage import utils



@rx.page(
    route=Route.INDEX.value,
    title=utils.INDEX_TITLE,
    description=utils.INDEX_DESCRIPTION,
    image=utils.INDEX_IMAGE,
    meta=utils.index_meta
)
def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),

        rx.center(
            rx.vstack(
                header(),
                index_links(),
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

