from fastapi import FastAPI

from src.stickers.api import router as stickers_router

ROUTERS = [stickers_router]


def create_app():
    app = FastAPI(
        title="Stickers App",
        description="An amazing sticker app",
        debug=True,
    )

    for router in ROUTERS:
        app.include_router(router)

    return app


app = create_app()
