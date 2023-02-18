import uvicorn as uvicorn
from fastapi import FastAPI, Depends, APIRouter
from sqlalchemy.orm import Session

from database import SessionLocal, engine
from home import models, schemas, service
from loby import service

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


home_router = APIRouter(
    prefix="/home",
    tags=["home"]
)

loby_router =APIRouter(
    prefix="/loby",
    tags=["loby"]
)


@app.get('/')
async def root():
    return {"message" : "hello! PTN!"}


@home_router.get('/game_manual')
async def get_manuel(db: Session = Depends(get_db)):
    manuel_ls = service.get_game_manuel(db=db)
    return manuel_ls


@home_router.get('/profile_image')
async def get_profile_image(db: Session = Depends(get_db)):
    profile_ls = service.get_profile_image(db=db)
    return profile_ls


@loby_router.get('/game_mode')
async def get_game_mode(db: Session = Depends(get_db)):
    game_mode_ls = service.get_game_mode(db=db)
    return game_mode_ls




if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=8080, reload=True)
