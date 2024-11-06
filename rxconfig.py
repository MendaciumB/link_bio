import reflex as rx

config = rx.Config(
    app_name="link_bio",
    cors_allowed_origins=[
        "http://localhost:3000",
        "http://localhost:3001",
        "http://localhost:8000",
        "http://localhost:8001",
        "https://link-bio-if4n.onrender.com"
    ],
    backend_host="https://link-bio-if4n.onrender.com",
    #backend_port=8000,
    #api_url="http://localhost:8000"
)