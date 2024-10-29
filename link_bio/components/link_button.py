import reflex as rx
from ..styles import styles

def link_button(title: str, body: str, image: str, url: str, is_external=True) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=styles.Size.LARGE.value,
                    height=styles.Size.LARGE.value,
                    margin=styles.Size.MEDIUM.value,
                    alt=title
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    align_items="start",
                    spacing=styles.Size.ZERO.value,
                    padding_right=styles.Size.SMALL.value
                    #margin=styles.Size.ZERO.value
                )
            )
        ),
        href=url,
        is_external=is_external,
        width="100%",
    )
    
