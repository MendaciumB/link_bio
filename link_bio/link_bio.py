import reflex as rx
from .styles import styles
from . import constants as const
from .pages.index import index
from .pages.courses import courses
from .api.api import repo
from .api.api import live


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    head_components=[
        rx.script(src=f"https://googletagmanager.com/gtag/js?id={const.G_TAG}"),
        rx.script(
            """
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'G-3YGHT3XJFS');
"""            
        )
    ]
)

app.api.add_api_route("/hello", repo)
app.api.add_api_route("/live/{user}", live)
