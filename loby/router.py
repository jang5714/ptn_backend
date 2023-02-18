from fastapi import APIRouter

loby_router = APIRouter(
    prefix="/loby",
    tags=["loby"]
)

@loby_router.get("/game_manual")
async def game_manual():
    return {"message" : "gamerule"}


@loby_router.get("/profile_image")
async def profile_image():
    return{"message" : "imagefile"}
