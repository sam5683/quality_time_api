from fastapi import FastAPI
from app.routes.quiz_routes import router as quiz_router

app = FastAPI()

app.include_router(quiz_router)
