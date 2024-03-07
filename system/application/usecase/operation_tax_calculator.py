from typing import Dict, List, Union

from system.application.dto.tax_dto import OperationTaxDto
from system.application.ports.usecase.operation_tax_calculator_port import (
    OperationTaxCalculatorPort,
)


class OperationTaxCalculatorUseCase(OperationTaxCalculatorPort):
    def __init__(self) -> None:
        self.loss = 0

    def caculate_tax(
        self,
        operations: List[Dict[str, Union[str, int, float]]],
    ) -> List[OperationTaxDto]:
        """
        Calculate tax given an operation list
        """
        raise Exception()
