from fastapi import FastAPI

from .routes import package_files

app = FastAPI()

app.include_router(package_files.router)
