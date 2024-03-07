from typing import Optional

from pydantic import Field, validator

from system.domain.constants.operation import OperationTax, OperationType
from system.domain.entity.base_entity import BaseEntity


class OperationEntity(BaseEntity):
    operation_type: OperationType = Field(description="Operaration Type information")
    unit_cost: float = Field(description="Cost per stock unit")
    quantity: int = Field(description="Stock Quantity per operation")
    tax: Optional[float] = Field(
        description="Tax to be paid on profit per sell operation",
        ge=0,
    )

    @property
    def total_cost(self) -> float:
        return self.quantity * self.unit_cost

    @validator("tax")
    def round_tax(cls, v: Optional[float]) -> Optional[float]:
        return round(v, OperationTax.ROUND.value) if v else v
