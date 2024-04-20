from fastapi import FastAPI

from app.routers import users, tours, wallets, beaches

app = FastAPI()


app.include_router(users.router)
app.include_router(tours.router)
app.include_router(wallets.router)
app.include_router(beaches.router)
