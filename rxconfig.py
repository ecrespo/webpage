import reflex as rx

config = rx.Config(
    app_name="webpage",
    api_url="https://webpage-production-9957.up.railway.app/",
    cors_allowed_origins=[
        "http://localhost:3000",
        "https://api.seraph13.dev",
        "https://webpage-production-9957.up.railway.app/"
    ],
)