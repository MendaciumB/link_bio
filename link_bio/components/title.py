import reflex as rx
from ..styles import styles

def title(text: str) -> rx.Component:
    return rx.heading(
        text,
        size="7",
        style=styles.title_style
    )









