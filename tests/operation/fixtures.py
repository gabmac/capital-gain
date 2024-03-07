from typing import Optional

from system.application.dto.tax_dto import OperationTaxDto
from system.domain.constants.operation import OperationType
from system.domain.entity.operation_entity import OperationEntity


class OperationEntityFixture:
    def __init__(
        self,
        operation_type: OperationType = OperationType.BUY.value,
        unit_cost: float = 10,
        quantity: float = 10,
        tax: Optional[float] = 0,
    ) -> None:
        self.operation_type = operation_type
        self.unit_cost = unit_cost
        self.quantity = quantity
        self.tax = tax

    @property
    def mock_operation(self) -> OperationEntity:
        return OperationEntity(
            operation_type=self.operation_type,
            unit_cost=self.unit_cost,
            quantity=self.quantity,
            tax=self.tax,
        )


class OperationTaxDTOFixture:
    def __init__(
        self,
        unit_cost: float = 10,
        quantity: float = 10,
        tax: Optional[float] = None,
    ) -> None:
        self.unit_cost = unit_cost
        self.quantity = quantity
        self.entity_fixture_buy = OperationEntityFixture(
            operation_type=OperationType.BUY.value,
            unit_cost=self.unit_cost,
            quantity=self.quantity,
            tax=0,
        )

        self.entity_fixture_sell = OperationEntityFixture(
            operation_type=OperationType.SELL.value,
            unit_cost=self.unit_cost,
            quantity=self.quantity,
            tax=tax,
        )

    @property
    def mock_buy_tax_value(self) -> OperationTaxDto:
        return OperationTaxDto.model_dump(self.entity_fixture_sell.mock_operation)

    @property
    def mock_sell_tax_value(self) -> OperationTaxDto:
        return OperationTaxDto.model_dump(self.entity_fixture_buy.mock_operation)
