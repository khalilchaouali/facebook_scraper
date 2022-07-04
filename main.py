import uvicorn as uvicorn
from router.v0.api import router
from fastapi import FastAPI

app = FastAPI()

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
