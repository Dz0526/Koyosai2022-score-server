from fastapi import FastAPI

from api.routers import ranking, user,score

app = FastAPI()

app.include_router(user.router)
app.include_router(score.router)
app.include_router(ranking.router)