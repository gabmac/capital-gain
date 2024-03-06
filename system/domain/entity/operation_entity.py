from pydantic import Field

from system.domain.constants.operation import OperationType
from system.domain.entity.base_entity import BaseEntity


class OperationEntity(BaseEntity):
    operation_type: OperationType = Field(description="Operaration Type information")
    unit_cost: float = Field(description="Cost per stock unit")
    quantity: float = Field(description="Stock Quantity per operation")
    tax: float = Field(description="Tax to be paid on profit per sell operation", ge=0)
