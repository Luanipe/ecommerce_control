import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import settings
from app.api.v1.routes import routers as v1_routers


class AppCreator:
    def __init__(self):
        self.app = FastAPI(
            title=settings.PROJECT_NAME,
            openapi_url=f"{settings.API}/openapi.json",
            version="0.0.1"
        )

        if settings.CORS_ORIGIN:
            self.app.add_middleware(
                CORSMiddleware,
                allow_origins=[],
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"]
            )

        @self.app.get("/")
        def root():
            return "Hello, world! Service is running!"

        self.app.include_router(v1_routers, prefix=settings.API_V1)


app_creator = AppCreator()
app = app_creator.app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


