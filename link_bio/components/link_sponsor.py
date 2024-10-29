import reflex as rx
from ..styles import styles

def link_sponsor(imagen: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=imagen,
            height="3.5em",
            width="auto",
            alt=alt
        ),
        href=url,
        is_external=True
    )