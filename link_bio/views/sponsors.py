import reflex as rx
from ..components.title import title
from ..components.link_sponsor import link_sponsor
from .. import constants as const
from ..styles import styles

def sponsors() -> rx.Component:
    return rx.vstack(
        title("Colaboran"),
        rx.flex(
            link_sponsor(
                "/elgato.png",
                const.ELGATO_URL,
                "Logotipo de Elgato"
            ),
            link_sponsor(
                "/mvp.png",
                const.MVP_URL,
                "Logotipo de Microsoft MVP"
            ),
            link_sponsor(
                "/githubstar.png",
                const.GITHUB_STAR_URL,
                "Logotipo de GitHub Star"
            ),
            spacing=styles.Size.BIG.value,
            flex_direction=["column","row", "row", "row", "row"],
        ),
        width="100%",
        align_items="start"
    )
