import reflex as rx
from ..components.link_button import link_button
from ..components.title import title
from ..styles import styles
from .. import constants as const
from ..routes import Route

def index_links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),

        link_button(
            "Cursos gratis", 
            "Consulta mis tutoriales para aprender programación",
            "/icons/code.svg",
            Route.COURSOS.value,
            is_external=False
        ),
        link_button(
            "Twitch", 
            "Tansmisiones sobre programación de lunes a viernes",
            "/icons/twitch.svg",
            const.TWITCH_URL
        ),
        link_button(
            "Youtube", 
            "Tutoriales sobre desarrollo de software semanales",
            "/icons/youtube.svg",
            const.YOUTUBE_URL
        ),
        link_button(
            "Discord", 
            "El chat y los grupos de estudio de la comunidad",
            "/icons/discord.svg",
            const.DISCORD_URL
        ),
        link_button(
            "Youtube [canal secundario]", 
            "Emisiones en directo destacadas",
            "/icons/youtube.svg",
            const.YOUTUBE_SECONDARY_URL
        ),
        
        title("Recursos y más"),

        link_button(
            "Git y GitHub desde cero", 
            "Aquí puedes comprar mi libro en formato físico y eBook",
            "/icons/git.svg",
            const.BOOK_URL
        ),
        link_button(
            "Libros recomendados", 
            "Mi listado de libros sobre programación, ciencia y tecnología",
            "/icons/book.svg",
            const.BOOKS_URL
        ),
        link_button(
            "Mi setup", 
            "Listado con todos los elementos que uso en mi trabajo",
            "/icons/setup.svg",
            const.SETUP_URL
        ),
        link_button(
            "MoureDev", 
            "Mi sitio Web",
            "/icons/logo.png",
            const.MOUREDEV_URL
        ),
        link_button(
            "Invítame a un café", 
            "¿Quieres ayudarme a que siga creando contenido?",
            "/icons/coffee.svg",
            const.COFFEE_URL
        ),

        title("Contacto"),
        link_button(
            "MyPublicInbox", 
            "Respuesta rápida y con preferencia",
            "/icons/email.svg",
            const.MYPUBLICINBOX_URL
        ),
        link_button(
            "Email",
            const.EMAIL,
            "/icons/checkemail.svg",
            f"mailto:{const.EMAIL}"
        ),
        width="100%",
        spacing=styles.Size.MEDIUM.value
    )
