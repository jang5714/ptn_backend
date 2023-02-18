from sqlalchemy.orm import Session

import database
from . import models, schemas
from .schemas import GameManuelCreate


def get_game_manuel(db: Session):
    return db.query(models.GameManuel).all()


def get_profile_image(db: Session):
    return db.query(models.ProfileImage).all()


# def get_profile_images(db: Session):
#     return db.query(homeModel.Profileimage).all()


