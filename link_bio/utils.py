import reflex as rx 



#Común

def lang() -> rx.Component:
    return rx.script("document.documentElement.lan='es'")

preview = "https://moure.dev/preview.jpg"

_meta=[
    {"name": "og:type", "content": "website",},
    {"name": "og:image", "content": preview},
    {"name": "twitter:card", "content": "summary_large_image"},
    {"name": "twitter:site", "content": "@mouredev"}
]


# Index


index_title = "MoureDev | Te enseño programación y desarrollo de software"
index_description = "Hola, mi nombre es Brais Moure. Soy ingeniero se software, desarrollador freelanc full-stack y divulgador."

index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description},
]

index_meta.extend(_meta)


# Cursos


courses_title = "MoureDev | Cursos gratis"
courses_description = "Este es un listado con algunos cursos gratis para aprender programación. Python, SQL, Git..."

courses_meta = [
    {"name": "og:title", "content": courses_title},
    {"name": "og:description", "content": courses_description},
]

courses_meta.extend(_meta)