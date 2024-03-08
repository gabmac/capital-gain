from typing import Optional

from pydantic import Field, field_validator

from system.domain.constants.operation import OperationTax, OperationType
from system.domain.entity.base_entity import BaseEntity


class OperationEntity(BaseEntity):
    type: OperationType = Field(
        description="Operaration Type information",
        alias="operation",
    )
    unit_cost: float = Field(description="Cost per stock unit", alias="unit-cost", ge=0)
    quantity: int = Field(description="Stock Quantity per operation", ge=0)
    tax: Optional[float] = Field(
        description="Tax to be paid on profit for sell operation",
        default=None,
        ge=0,
    )

    @property
    def total_cost(self) -> float:
        return self.quantity * self.unit_cost

    @field_validator("tax", mode="before")
    def round_tax(cls, v: Optional[float]) -> Optional[float]:
        return round(v, OperationTax.ROUND.value) if v else v
