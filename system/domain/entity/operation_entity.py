from typing import Optional

from pydantic import Field, field_validator

from system.domain.constants.operation import OperationTax, OperationType
from system.domain.entity.base_entity import BaseEntity


class OperationEntity(BaseEntity):
    operation_type: OperationType = Field(
        description="Operaration Type information",
        alias="operation",
    )
    unit_cost: float = Field(description="Cost per stock unit", alias="unit-cost")
    quantity: int = Field(description="Stock Quantity per operation")
    tax: Optional[float] = Field(
        description="Tax to be paid on profit per sell operation",
        default=None,
    )

    @property
    def total_cost(self) -> float:
        return self.quantity * self.unit_cost

    @field_validator("tax", mode="before")
    def round_tax(cls, v: Optional[float]) -> Optional[float]:
        return round(v, OperationTax.ROUND.value) if v else v
