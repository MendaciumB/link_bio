import reflex as rx
from ..styles import styles
from ..styles.colors import Color
from ..routes import Route
from ..components.ant_components import float_button
from .. import constants as const

def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.box(
                rx.text(
                    "moure",
                    as_="span",
                    color=Color.PRIMARY.value
                ),
                rx.text(
                    "dev",
                    as_="span",
                    color=Color.SECONDARY.value
                ),
                style=styles.navbar_title_style
            ),
            href=Route.INDEX.value
        ),
        float_button(
            icon=rx.image(src="/icons/donate.svg"),
            href=const.COFFEE_URL
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=styles.Size.BIG.value,
        padding_y=styles.Size.DEFAULT.value,
        z_index="999",
        top="0"
    ) 