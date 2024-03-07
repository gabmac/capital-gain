from enum import Enum


class OperationType(Enum):
    BUY = "buy"
    SELL = "sell"


class OperationTax(Enum):
    ROUND = 2
