from enum import Enum


class OperationType(Enum):
    BUY = "buy"
    SELL = "sell"


class OperationTax(Enum):
    ROUND = 2
    TAX_PERCENT = 0.2
    MINIMUM_THRESHOLD = 20000
