from fastapi import APIRouter

from app.api.v1.endpoints.auth import router as auth_router
from app.api.v1.endpoints.category import router as category_router


routers = APIRouter()

v1_router_list = [auth_router, category_router]

for router in v1_router_list:
    routers.include_router(router, tags=["v1"])
