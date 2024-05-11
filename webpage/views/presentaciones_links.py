import reflex as rx

from webpage.components.link_button import link_button
from webpage.components.select_presentation import select_presentation
from webpage.components.timeline_component import timeline
from webpage.components.title import title
from webpage.constants import *
from webpage.styles.styles import Size
from webpage.views.routes import Route
from webpage.styles import styles


#with open("js/timeline.js", "r") as f:
#    timeline_js = f.read()


def presentaciones_links()-> rx.Component:
    return rx.vstack(
        title("Presentaciones"),
        link_button("LinkedIn", "Perfil de linkedin", LINKEDIN_URL, "/icons/linkedin.svg"),
        link_button("Twitter", "Mi cuenta de twitter", TWITTER_URL, "/icons/x.svg"),

        widht="100%",
        spacing="3",

    )