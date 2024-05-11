import reflex as rx
from pydantic import HttpUrl

from webpage.styles import styles
from webpage.styles.styles import Size


def link_button(title:str,body:str,url:HttpUrl,image:str,is_external=True) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    alt=f"Imagen del botón de {title}",
                    widht=Size.LARGE.value,
                    height=Size.LARGE.value,
                    margin=Size.MEDIUM.value,
                    # padding=Size.LARGE.value,
                ),
                rx.vstack(
                    rx.text(
                        title,
                        style=styles.button_title_style
                    ),
                    rx.text(
                        body,
                        style=styles.button_body_style
                    ),
                    padding_y=Size.SMALL.value,
                    padding_right=Size.SMALL.value,
                    spacing="0",
                    aling_items="start",
                    margin=Size.ZERO.value,
                ),
                widht="100%",
                padding_top=Size.MEDIUM.value,
                padding_bottom=Size.MEDIUM.value,
            )
        ),
        href=url,
        is_external=is_external,
        width="100%",
        height="100%",
    )

