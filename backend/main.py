import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
async def hello():
    return {"hello": "hello"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        debug=True,
        workers=4,
    )
