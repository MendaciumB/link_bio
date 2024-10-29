import reflex as rx
from ..views.navbar import navbar
from ..views.header import header
from ..views.index_links import index_links
from ..views.footer import footer
from ..views.sponsors import sponsors
from ..styles import styles
from .. import utils
from ..routes import Route


@rx.page(
        route=Route.INDEX.value,
        title=utils.index_title,
        description=utils.index_description,
        image=utils.preview,
        meta=utils.index_meta
)
def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                index_links(),
                sponsors(),
                align="center",
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=styles.Size.BIG.value,
                padding=styles.Size.BIG.value
            )
        ),
        footer(),
    )

