from fastapi import FastAPI

from hello_world.routers.default import router as default_router

app = FastAPI(
    title="Hello world!"
)

app.include_router(default_router)
