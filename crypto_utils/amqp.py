from enum import Enum

class ExchangeName(Enum):
    Crypto_Trade = "crypto_trade"


class QueueType(Enum):
    User_Handler = "user_handler"
    Status_Checker = "status_checker"
    Mother_User_Update = "mother_user_update"
    User_Update = "user_update"
    Orders = "orders"
    Backend_Update = "backend_update"


class MessageType(Enum):
    New_Order = "new_order"
    Cancel_Order = "cancel_order"
    Leverage_Change = "leverage_change"
    Margin_Change = "margin_change"
    Account_Update = "account_update"
    Status_Change = "status_change"
    Mother_User_Update = "mother_user_update"
    User_Update = "user_update"
    Backend_Update = "backend_update"


class BackendUpdateType(Enum):
    New_Order = "new_order"
    Leverage_Change = "leverage_change"
    Margin_Change = "margin_change"
    Account_Update = "account_update"
    Status_Change = "status_change"
