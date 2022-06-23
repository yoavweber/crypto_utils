from typing import TypedDict, List, get_type_hints
from enum import Enum


class Side(Enum):
    Buy = "BUY"
    Sell = "SELL"


class Market_Type(Enum):
    Futures = "futures"
    Spot = "spot"
    Margin = "margin"


# deprecated
class Binance_Market(Enum):
    Spot = "binance.com"
    Spot_Test = "binance.com-testnet"
    Margin = "binance.com-margin"
    Margin_Test = "binance.com-margin-testnet"
    Futures = "binance.com-futures"
    Futures_Test = "binance.com-futures-testnet"


class Order_Type(Enum):
    Market = "MARKET"
    Limit = "LIMIT"
    #  futures
    Stop = "STOP"
    Stop_Market = "STOP_MARKET"
    Take_Profit_Market = "TAKE_PROFIT_MARKET"
    Take_Profit = "TAKE_PROFIT"
    #
    Stop_Loss = "STOP_LOSS"
    Stop_Loss_Limit = "STOP_LOSS_LIMIT"
    Take_Profit_Limit = "TAKE_PROFIT_LIMIT"
    Limit_Maker = "LIMIT_MAKER"


class Event_Type(Enum):
    Futures_Order = "ORDER_TRADE_UPDATE"
    Spot_Order = "executionReport"
    Account_Futures = "ACCOUNT_UPDATE"
    Account_Spot = "outboundAccountPosition"
    Leverage_Change = "ACCOUNT_CONFIG_UPDATE"


class Order_Status(Enum):
    New = "NEW"
    Filled = "FILLED"
    Canceled = "CANCELED"
    Expired = "EXPIRED"


class FuturesEvent(TypedDict):
    stream_type: str
    event_type: str
    event_time: int
    symbol: str
    side: Side
    trade_id: int
    order_price: str
    order_quantity: str
    buyer_order_id: int
    order_id: str
    client_order_id: str
    seller_order_id: int
    trade_time: int
    is_market_maker: bool
    ignore: bool
    order_type: str
    reduce_only: bool
    current_order_status: str
    market_type: Market_Type
    transaction_time: int


class Futures_Balance(TypedDict, total=False):
    asset: str
    wallet_balance: str
    cross_wallet_balance: str


class Future_Asset(TypedDict):
    accountAlias: str
    asset: str
    balance: str
    withdrawAvailable: str
    updateTime: int


class Futures_Account_Event(TypedDict, total=False):
    stream_type: Event_Type
    event_type: Event_Type
    event_time: int
    transaction: int
    event_reason: str
    balances: List[Futures_Balance]
    symbol: str
    side: Side
    trade_id: int
    price: str
    order_quantity: str
    buyer_order_id: int
    seller_order_id: int
    trade_time: int
    is_market_maker: bool
    ignore: bool
    order_type: str
    current_order_status: str
    unicorn_fied: List[str]


class Cancel_Order(TypedDict):
    symbol: str
    client_order_id: str


class Work_Type(Enum):
    New_Order = "NEW"
    Cancel_Order = "CANCEL"
    Order_Status = "STATUS"


class Update_Order(TypedDict):
    market_type: Market_Type
    status: Order_Type
    symbol: str
    clientOrderId: str
    work_type: str
    userId: str


class Futures_Position(TypedDict):
    symbol: str
    positionAmt: str
    entryPrice: str
    markPrice: str
    unRealizedProfit: str
    liquidationPrice: str
    leverage: str
    maxNotionalValue: str
    marginType: str
    isolatedMargin: str
    isAutoAddMargin: str
    positionSide: str
    notional: str
    isolatedWallet: str
    updateTime: int


class Leverage_Change(TypedDict):
    stream_type: str
    event_type: str
    event_time: int
    symbol: str
    leverage: int
    market_type: str


class User_Old:
    def __init__(self, id, api_key, api_secret, name, email, is_mother):
        self.id = id
        self.name = name
        self.api_key = api_key
        self.api_secret = api_secret
        self.name = name
        self.email = email
        self.is_mother = is_mother

    id = ""
    name = ""
    api_key = ""
    api_secret = ""
    email = ""
    is_mother = ""


class Order:
    binance_id = ""
    price = ""
    quantity = ""
    side = ""
    order_status = ""
    symbol = ""
    order_type = ""
    user = ""
    mother_user_order_id = ""
    market_type = ""



class UserDict(TypedDict):
    name: str
    id: str
    name: str
    api_key: str
    api_secret: str
    email: str
    is_mother: bool

class User:
    name: str
    id: str
    name: str
    api_key: str
    api_secret: str
    email: str
    is_mother: bool

    def __init__(self, data: UserDict):
        for k, _ in get_type_hints(self).items():
            setattr(self, k, data[k])
