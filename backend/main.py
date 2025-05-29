import uvicorn
from fastapi import FastAPI, Depends
from typing_extensions import Annotated
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from config import settings
import app.core.dependencies as dependencies

from app.models.user import User

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

# @app.get("/")
# def hello(db: Annotated[Session, Depends(dependencies.get_db_session)]):
#     res = db.query(User).all()
#     return {"users": res}


app_creator = AppCreator()
app = app_creator.app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


