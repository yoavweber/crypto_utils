import os
from crypto_utils.types import *
import requests as r
import json
from unicorn_fy.unicorn_fy import UnicornFy  # type: ignore


def is_development() -> bool:
    if os.getenv("APP_ENV") != "prod":
        return True
    return False


def parse_deserializer(data) -> UserDict:
    """adding the id to the fields to easily create objects"""
    new_data = data["fields"]
    new_data["id"] = data["pk"]
    return new_data


def res_to_user_list(res: r.Response) -> List[UserDict]:
    """parsing backend response to list of user dict"""
    users_string = res.json()
    users_raw = json.loads(users_string)
    users = list(map(lambda user: parse_deserializer(user), users_raw))
    return users


def get_user_market(user: User) -> Market_Type:
    user_market = user.name.split("_")[0]
    if user_market == Market_Type.Futures.value:
        return Market_Type.Futures
    return Market_Type.Spot


def get_event_parser(market):
    parser_to_function = {
        "binance.com-futures": UnicornFy.binance_com_futures_websocket,
        "binance.com": UnicornFy.binance_com_websocket,
    }
    return parser_to_function[market]


def format_child_order_id(mother_order_id: str, user: User):
    """formating user id from mother id and user apikey and name to communicate across services"""
    short_api_key = user.api_key[:10]
    order_id = mother_order_id + "_" + short_api_key
    if len(order_id) > 35:
        return order_id[:34]
    return order_id

def adjust_margin_type_to_binance_api(margin_type:str) -> Margin_Type_Enum:
    if margin_type == "cross":
        return Margin_Type_Enum.Crossed
    elif  margin_type == "isolated":
        return Margin_Type_Enum.Isolated
    else:
        raise Exception(f"unkown margin type value: {margin_type}" )