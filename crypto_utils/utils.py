import os
from crypto_utils.types import *
import requests as r
import json 

def is_development() -> bool:
    if os.getenv("APP_ENV") != "prod":
        return True
    return False

def parse_deserializer(data) -> UserDict:
    '''adding the id to the fields to easily create objects'''
    new_data = data["fields"]
    new_data["id"] = data["pk"]
    return new_data



def res_to_user_list(res: r.Response) -> List[UserDict]:
    '''parsing backend response to list of user dict'''
    users_string = res.json()
    users_raw = json.loads(users_string)
    users = list(map(lambda user: parse_deserializer(user), users_raw))
    return users


def get_user_market(user: User) -> Market_Type:
    user_market = user.name.split("_")[0]
    if user_market == Market_Type.Futures.value:
        return Market_Type.Futures
    return Market_Type.Spot



