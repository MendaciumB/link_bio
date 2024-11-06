from .. import constants as const
from .TwitchAPI import TwitchAPI


TWITCH_API = TwitchAPI()

async def repo() -> str:
    return const.REPO_URL

async def live(user: str) -> bool:
    if user == "mouredev":
        return False
    return True

    #return TWITCH_API.live(user)