from typing import List, Optional

from system.application.dto.tax_dto import OperationTaxDto
from system.domain.constants.operation import OperationTax, OperationType
from system.domain.entity.operation_entity import OperationEntity


class OperationEntityFixture:
    def __init__(
        self,
        operation_type: OperationType = OperationType.BUY.value,
        unit_cost: float = 4,
        quantity: float = 100000,
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

    @property
    def mock_sell_with_profit(self) -> List[OperationEntity]:
        buy_operation = OperationEntity(
            operation_type=OperationType.BUY.value,
            unit_cost=self.unit_cost,
            quantity=self.quantity,
            tax=self.tax,
        )
        sell_operation_profit = OperationEntity(
            operation_type=OperationType.SELL.value,
            unit_cost=self.unit_cost * 2,
            quantity=self.quantity,
            tax=OperationTax.TAX_PERCENT.value * self.unit_cost * self.quantity,
        )

        return [
            buy_operation,
            sell_operation_profit,
        ]


class OperationTaxDTOFixture:
    def __init__(
        self,
        unit_cost: float = 4,
        quantity: float = 100000,
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
        return OperationTaxDto.model_validate(self.entity_fixture_buy.mock_operation)

    @property
    def mock_sell_tax_value(self) -> OperationTaxDto:
        tax = (
            self.entity_fixture_sell.mock_operation.tax
            if self.entity_fixture_sell.mock_operation.tax
            else 0
        )
        return OperationTaxDto(tax=tax)

    @property
    def mock_sell_with_profit(self) -> List[OperationTaxDto]:
        return [
            OperationTaxDto.model_validate(operation)
            for operation in self.entity_fixture_buy.mock_sell_with_profit
        ]
