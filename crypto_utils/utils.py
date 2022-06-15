import os
from crypto_utils.types import *

def is_development() -> bool:
    if os.getenv("APP_ENV") != "prod":
        return True
    return False




def get_user_market(user: User) -> Market_Type:
    user_market = user.name.split("_")[0]
    if user_market == Market_Type.Futures.value:
        return Market_Type.Futures
    return Market_Type.Spot
