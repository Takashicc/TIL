from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from .routers import article

app = FastAPI()
app.include_router(article.router)


@app.get("/")
def root():
    return RedirectResponse("/docs")
