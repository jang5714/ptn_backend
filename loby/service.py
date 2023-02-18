from sqlalchemy.orm import Session
import database
from . import models, schemas


def get_game_mode(db: Session):
    return db.query(models.GameMode).all()


def get_game_room(db: Session):
    return db.query(models.GameRoom).all()