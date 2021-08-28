from fastapi import FastAPI

from src.user.routers import router as user_router

app = FastAPI(docs_url="/api/swagger")

app.include_router(user_router, prefix="/api/users")
