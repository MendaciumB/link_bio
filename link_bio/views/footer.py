import reflex as rx
import datetime
from .. import constants as const
from ..styles import styles
from ..styles.colors import TextColor
from ..styles.styles import Size

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/logo.png",
            height=styles.Size.VERY_BIG.value,
            weight=styles.Size.VERY_BIG.value,
            alt="Logotipo de MoureDev. una \"eme\" entre llaves."
        ),
        rx.link(
            f"@ 2014-{datetime.date.today().year} MOUREDEV BY BRAIS MOURE V3.",
            href=const.MOUREDEV_URL,
            is_external=True,
            font_size=styles.Size.MEDIUM.value,
            margin_top=Size.DEFAULT.value
        ),
        rx.link(
            rx.hstack(
                rx.image(
                    src="/icons/github.svg",
                    height=Size.LARGE.value,
                    width=Size.LARGE.value
                ),
                rx.text(
                    "BUILDING SOFTWARE WITH <3 FROM GALICIA TO THE WORLD. By Brayhan.",
                    font_size=styles.Size.MEDIUM.value,
                ),
                #margin_top=styles.Size.ZERO.value
            ),
            href=const.REPO_URL,
            is_external=True,
        ),
        align="center",
        margin_botton=styles.Size.BIG.value,
        padding_bottom=styles.Size.DEFAULT.value,
        padding_x=styles.Size.BIG.value,
        color=TextColor.BODY.value,
        spacing="-5px"
    )