from typing import TypedDict, List
from enum import Enum


class Side(Enum):
    Buy = "BUY"
    Sell = "SELL"


class Work_Type(Enum):
    New_Order = "new_order"
    Account_Update = "account_update"
    Status_Change = "status_change"


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
    market_type: str
    transaction_time: int


class Futures_Balance_Raw(TypedDict, total=False):
    asset: str
    wallet_balance: str
    cross_wallet_balance: str


class Future_Asset(TypedDict):
    accountAlias: str
    asset: str
    balance: str
    withdrawAvailable: str
    updateTime: int


class Spot_Balance(TypedDict):
    asset: str
    free: str
    locked: str


class Futures_Balance(TypedDict):
    asset: str
    withdrawAvailable: str
    balance: str


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

class Account_Update_Position(TypedDict):
    symbol: str
    position_amount: str
    entry_price: str
    accumulated_realized: str
    upnl: str
    margin_type: str
    isolated_wallet: str
    position_side: str

class Account_Update_Futures(TypedDict):
    stream_type: str
    event_type: str
    event_time: float
    transaction: float
    event_reason: float
    balances: List[Futures_Balance_Raw]
    positions: List[Account_Update_Position]


