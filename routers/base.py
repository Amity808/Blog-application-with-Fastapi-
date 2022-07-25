from fastapi import APIRouter

from routers import blog, user, authentication


api_router = APIRouter()

api_router.include_router(authentication.router, prefix="/login", tags=["Authentication"])
api_router.include_router(blog.router, prefix="/blog", tags=["blog"])
api_router.include_router(user.router, prefix="/users", tags=["users"])
