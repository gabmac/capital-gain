from typing import Dict, List, Union

from system.application.dto.tax_dto import OperationTaxDto
from system.application.ports.usecase.operation_tax_calculator_port import (
    OperationTaxCalculatorPort,
)
from system.domain.constants.operation import OperationTax, OperationType
from system.domain.entity.operation_entity import OperationEntity


class OperationTaxCalculatorUseCase(OperationTaxCalculatorPort):
    def __init__(self) -> None:
        self.balance = 0.0
        self._weighted_average_price = 0.0
        self._quantity = 0

    def caculate_tax(
        self,
        operations: List[Dict[str, Union[str, int, float]]],
    ) -> List[OperationTaxDto]:
        """
        Calculate tax given an operation list
        """
        tax_list = []
        for operation in operations:
            operation_entity = OperationEntity.model_validate(operation)
            self._update_weighted_average_price(operation=operation_entity)
            self._update_quantity(operation=operation_entity)
            if self._operation_under_threshold(
                operation=operation_entity,
            ) or self._operation_type_is_not_applicable(operation=operation_entity):
                operation_entity.tax = 0
            else:
                operation_entity.tax = self._calculate_tax(operation=operation_entity)

            self._update_balance(operation=operation_entity)

            tax_list.append(
                OperationTaxDto.model_validate(operation_entity),
            )

        return tax_list

    def _operation_under_threshold(self, operation: OperationEntity) -> bool:
        return OperationTax.MINIMUM_THRESHOLD.value >= operation.total_cost

    def _operation_type_is_not_applicable(self, operation: OperationEntity) -> bool:
        return operation.operation_type.value == OperationType.SELL.value

    def _balance_not_enough(self) -> bool:
        return self.balance >= 0

    def _update_weighted_average_price(self, operation: OperationEntity) -> None:
        if operation.operation_type.value == OperationType.BUY.value:
            if not self._weighted_average_price or not self._quantity:
                self._weighted_average_price = operation.unit_cost
            else:
                self._weighted_average_price = (
                    self._quantity * self._weighted_average_price + operation.total_cost
                ) / (self._quantity + operation.quantity)

    def _update_quantity(self, operation: OperationEntity) -> None:
        added_quantity = (
            operation.quantity
            if operation.operation_type.value == OperationType.BUY.value
            else -operation.quantity
        )
        self._quantity += added_quantity

    def _update_balance(self, operation: OperationEntity) -> None:
        if operation.operation_type.value == OperationType.SELL.value:
            value = self._weighted_average_price * self._quantity - operation.total_cost
            self.balance = self.balance + value

    def _calculate_tax(self, operation: OperationEntity) -> float:
        loss = self.balance if self.balance < 0 else 0
        tax = OperationTax.TAX_PERCENT.value * (
            (operation.unit_cost - self._weighted_average_price) * operation.quantity
            + loss
        )
        return tax if tax > 0 else 0
