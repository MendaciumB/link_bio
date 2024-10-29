import reflex as rx
from ..styles import styles

def link_icon(image: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            width=styles.Size.DEFAULT.value,
            alt=alt
        ),
        href=url,
        is_external=True
    )