from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers import  user,score,ranking

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(score.router)
app.include_router(ranking.router)