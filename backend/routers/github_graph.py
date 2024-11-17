import requests
from fastapi import APIRouter

from backend.config import settings
from backend.utils import add_users_data, get_followers

github_router = APIRouter(prefix='/github', tags=['Github'])


@github_router.get("/{username}")
async def root(username: str = "x4nth055"):
    token = settings.GITHUB_API_TOKEN
    headers = {
        "authorization": f"token {token}"
    } if token else {}

    url = f"https://api.github.com/users/{username}/followers"

    # Делаем запрос и получаем ответ
    response = requests.get(url, headers=headers)

    if response.status_code == 200:  # Проверка кода ответа
        rj = response.json()
        add_users_data(rj, headers=headers, depth=0)
        return rj
    elif response.status_code == 404:
        return {"status": 401,
                "message": "Ай-ай-ай, неверный токен авторизации!"}  # Отправляем своё сообщение и код ошибки
    else:
        return response.json()


@github_router.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}!"}
