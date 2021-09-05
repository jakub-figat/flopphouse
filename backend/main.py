from fastapi import FastAPI

from src.apps.user.routers import router as user_router

app = FastAPI(
    title="FloppHouse - Social app",
    description="An application that makes communicating easier",
    version="0.1.0",
    docs_url="/api/v1/swagger",
)

app.include_router(user_router, prefix="/api/v1/users")
