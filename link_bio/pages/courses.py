import reflex as rx
from ..views.navbar import navbar
from ..views.header import header
from ..views.courses_links import courses_links
from ..views.footer import footer
from ..views.sponsors import sponsors
from ..styles import styles
from .. import utils
from ..routes import Route


@rx.page(
        route=Route.COURSOS.value,
        title=utils.courses_title,
        description=utils.courses_description,
        image=utils.preview,
        meta=utils.courses_meta
)
def courses() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(details=False),
                courses_links(),
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

