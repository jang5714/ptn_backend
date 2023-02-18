from fastapi import APIRouter

home_router = APIRouter(
    prefix="/home",
    tags=["home"]
)

@home_router.get("/game_manual")
async def game_manual():
    return {"message" : "gamerule"}


@home_router.get("/profile_image")
async def profile_image():
    return{"message" : "imagefile"}
