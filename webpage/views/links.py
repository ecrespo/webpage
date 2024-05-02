import reflex as rx

from webpage.components.link_button import link_button
from webpage.components.title import title
from webpage.constants import *

def links()-> rx.Component:
    return rx.vstack(
        title("Mis redes"),
        link_button("LinkedIn","Perfil de linkedin",LINKEDIN_URL,"icons/linkedin.svg"),
        link_button("Twitter","Mi cuenta de twitter",TWITTER_URL,"icons/x.svg"),
        title("Mis recursos"),
        link_button("Github", "Mi cuenta de github", GITHUB_URL,"icons/github.svg"),
        link_button("Gitlab", "Mi cuenta de gitlab", GITLAB_URL,"icons/square-gitlab.svg"),
        link_button("Medium", "Mi cuenta de github", MEDIUM_URL,"icons/medium.svg"),
        title("Contacto"),
        link_button("Mi sitio web", "Mi página web", PAGINA_URL,"icons/code.svg"),
        link_button("Email", f"{EMAIL}", f"mailto:<{EMAIL}>","icons/email.svg"),
        widht="100%",
        spacing="3",

    )
