from fastapi import FastAPI

from app.routers import users, tours, wallets, beaches
from app.tags_metadata import tags_metadata

app = FastAPI(
    swagger_ui_parameters={"syntaxHighlight.theme": "nord"},
    openapi_tags=tags_metadata,
)


app.include_router(users.router)
app.include_router(tours.router)
app.include_router(wallets.router)
app.include_router(beaches.router)
