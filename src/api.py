from fastapi import FastAPI

from routers import characters
from routers import episodes

app = FastAPI()

app.include_router(characters.router)
app.include_router(episodes.router)
