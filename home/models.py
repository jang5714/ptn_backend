from sqlalchemy import Boolean, Column, Integer, String
from database import Base

# Models
class GameManuel(Base):
    __tablename__ = "game_manuel"

    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String, index=True)
    script = Column(String, index=True)


class ProfileImage(Base):
    __tablename__ = "profile_image"

    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String, index=True)


class GameRoom(Base):
    __tablename__ = "game_room"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, index=True)
    user_type = Column(Integer, index=True)
    image_url = Column(String, index=True)
