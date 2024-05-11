import reflex as rx

from webpage.styles.colors import Color


class FloatButton(rx.Component):
    library = "antd"
    tag = "FloatButton"
    icon = rx.image(src="/icons/code.svg")
    href = "https://www.seraph.to"
    target = "_blank"
    badge = {"dot": True, "color": Color.PRIMARY.value}
    

float_button = FloatButton.create
