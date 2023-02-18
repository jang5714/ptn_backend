from sqlalchemy import Boolean, Column, Integer, String
from database import Base

# Models
class GameMode(Base):
    __tablename__ = "game_mode"

    id = Column(Integer, primary_key=True, index=True)
    image = Column(String, index=True)
    title = Column(String, index=True)
    text = Column(String, index=True)

class GameRoom(Base):
    __tablename__ = "game_room"

    id = Column(Integer, primary_key=True, index=True)
    image = Column(String, index=True)
    user_name = Column(String, index=True)
    user_type = Column(String, index=True)
