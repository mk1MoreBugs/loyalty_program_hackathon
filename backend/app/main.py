from fastapi import FastAPI

from app.routers import users, tours

app = FastAPI()


app.include_router(users.router)
app.include_router(tours.router)
