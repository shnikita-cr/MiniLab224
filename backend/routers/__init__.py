from fastapi import FastAPI
from fastapi.routing import APIRouter

from .github_graph import github_router
from ..config import settings


def init_app(app: FastAPI):
    """
    Здесь прописываем роутеры, которые нужно включить в приложение
    """
    router = APIRouter(prefix=settings.URL_PREFIX)
    router.include_router(github_router)
    app.include_router(router)
