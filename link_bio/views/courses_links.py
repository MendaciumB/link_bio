import reflex as rx
from ..components.link_button import link_button
from ..components.title import title
from ..styles import styles
from .. import constants as const
from ..routes import Route

def courses_links() -> rx.Component:
    return rx.vstack(
        title("Cursos gratis"),

        link_button(
            "Retos de programación", 
            "Ruta de estudio semanal para practicar lógica de programación",
            "/icons/code.svg",
            const.CODE_CHALLENGES_URL
        ),
        link_button(
            "Python desde cero", 
            "Curso de +37h: fundamentos, frontend, backend, testing...",
            "/icons/python.svg",
            const.PYTHON_COURSE_URL
        ),
        link_button(
            "Git y GitHub", 
            "Curso de 5h para aprender Git y GitHub desde cero",
            "/icons/git.svg",
            const.GIT_COURSE_URL
        ),
        link_button(
            "SQL y Bases de Datos", 
            "Curso de 7h desde cero para aprender los dunfamentos de SQL",
            "/icons/sql.svg",
            const.SQL_COURSE_URL
        ),
        link_button(
            "Un día, un lenguaje", 
            "Primeros pasos en los 11 lenguajes de programación más usados",
            "/icons/code.svg",
            const.LANGUAGES_COURSE_URL
        ),

        title("Mucho más en:"),

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
        width="100%",
        spacing=styles.Size.MEDIUM.value
    )
