from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend import routers
from backend.config import settings
import uvicorn

app = FastAPI()

if len(settings.CORS_ORIGINS) > 0:
    app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True,
                       allow_methods=['*'], allow_headers=['*'])
routers.init_app(app)

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=settings.PORT, reload=True)
