from typing import Union, Optional
from pydantic import BaseModel


class GameManuelBase(BaseModel):
    """
    Base
    """
    imageUrl: Optional[str]
    script: str


class GameManuelCreate(GameManuelBase):
    """
    Setter
    """
    pass


class GameManuel(GameManuelBase):
    """
    Getter
    """
    id: int

    class Config:
        orm_mde = True


class ProfileImageBase(BaseModel):
    """
    Getter
    """
    imageUrl: Optional[str]


class ProfileImageCreate(ProfileImageBase):
    """
    Getter
    """
    pass


class ProfileImage(ProfileImageBase):
    """
    Getter
    """
    id: int

    class Config:
        orm_mode = True


class GameRoomBase(BaseModel):
    """
    Getter
    """
    imageUrl: Optional[str]


class GameRoomCreate(GameRoomBase):
    """
    Getter
    """
    pass


class GameRoom(GameRoomBase):
    """
    Getter
    """
    id: int

    class Config:
        orm_mode = True