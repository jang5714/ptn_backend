from typing import Union, Optional
from pydantic import BaseModel


class GameModeBase(BaseModel):
    """
    Base
    """
    image: Optional[str]
    title: str
    text: str


class GameModeCreate(GameModeBase):
    """
    Setter
    """
    pass


class GameMode(GameModeBase):
    """
    Getter
    """
    id: int

    class Config:
        orm_mde = True

from typing import Union, Optional
from pydantic import BaseModel


class GameRoomBase(BaseModel):
    """
    Base
    """
    image: Optional[str]
    user_name: str
    user_type: str


class GameRoomCreate(GameRoomBase):
    """
    Setter
    """
    pass


class GameRoom(GameRoomBase):
    """
    Getter
    """
    id: int

    class Config:
        orm_mde = True




