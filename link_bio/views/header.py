import reflex as rx
from ..components.link_icon import link_icon
from ..styles import styles
from ..components.info_text import info_text
from ..styles.colors import TextColor
from ..styles.colors import Color
from .. import constants as const

def header(details = True) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name="Brais Moure", 
                size="7",
                src="/avatar.jpg",
                color=TextColor.BODY.value,
                bg=Color.CONTENT.value,
                padding="2px",
                border="4px",
                border_color=Color.PRIMARY.value,
                radius="full"

            ),
            rx.vstack(
                rx.heading("BRAIS MOURE"),
                rx.text(
                    "@mouredev",
                    margin_top=styles.Size.ZERO.value,
                    color=TextColor.BODY.value
                ),
                rx.hstack(
                    link_icon(
                        "/icons/github.svg",
                        const.GITHUB_URL,
                        "Github"
                    ),
                    link_icon(
                        "/icons/x.svg",
                        const.TWITTER_X_URL,
                        "Twitter/X"
                    ),
                    link_icon(
                        "/icons/instagram.svg",
                        const.INSTAGRAM_URL,
                        "instagram"
                    ),
                    link_icon(
                        "/icons/tiktok.svg",
                        const.TIKTOK_URL,
                        "TikTok"
                    ),
                    link_icon(
                        "/icons/spotify.svg",
                        const.SPOTIFY_URL,
                        "Spotify"
                    ),
                    link_icon(
                        "/icons/linkedin.svg",
                        const.LINKEDIN_URL,
                        "LinkedIn"
                    ),
                    spacing=styles.Size.MEDIUM.value
                ),
            ),
            spacing=styles.Size.MEDIUM.value
        ),
        rx.cond(
            details,
            rx.vstack(
                rx.flex(
                    info_text("+13", "años de experiencia"),
                    rx.spacer(),
                    info_text("100+", "aplicaciones creadas"),
                    rx.spacer(),
                    info_text("1M+", "seguidores"),
                    width="100%"
                ),
                rx.text(
                    """Soy ingeniero de software desde hace más de 13 años.
                    Actualmente trabajo como freelance full-stack developer iOS y Android.
                    Además creo contenido formativo sobre programación y tecnología en redes.
                    Aquí podrás encontrar todos mis enlaces de interés. ¡Bienvenid@!
                    """,
                    font_size=styles.Size.DEFAULT.value,
                    color=TextColor.BODY.value
                ),
                width="100%",
                spacing=styles.Size.BIG.value
            )
        ),
        spacing=styles.Size.BIG.value,
        align="center",
        align_items="start",
        width="100%"
    )