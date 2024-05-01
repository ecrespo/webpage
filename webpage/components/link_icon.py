import reflex as rx
from pydantic import HttpUrl

import webpage.styles.styles as styles

def link_icon(image:str,url: HttpUrl,alt:str)-> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            alt=alt,
            height=styles.Size.DEFAULT.value,
            width=styles.Size.DEFAULT.value,
        ),
        href=url,
        is_external=True
    )
