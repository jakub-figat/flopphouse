from fastapi import FastAPI

from src.database import close_mongo_connection, start_mongo_connection
from src.user.routers import router as user_router

app = FastAPI(
    title="FloppHouse - Social app",
    description="An application that makes communicating easier",
    version="0.1.0",
    docs_url="/api/v1/swagger",
    on_startup=[start_mongo_connection],
    on_shutdown=[close_mongo_connection],
)

app.include_router(user_router, prefix="/api/v1/users")
