import reflex as rx
from ..styles import styles
from ..styles.colors import TextColor
from ..styles.colors import Color

def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.text(
            title,
            font_weight="bold", 
            color=Color.PRIMARY.value,
            as_="span"
        ),
        body,
        font_size=styles.button_body_style,
    )
