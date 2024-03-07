import json
from typing import List, Optional, Type

from system.application.dto.tax_dto import OperationTaxDto
from system.application.ports.inputs.inputs_port import ReadInputPort
from system.application.ports.usecase.operation_tax_calculator_port import (
    OperationTaxCalculatorPort,
)


class ReadStdIn(ReadInputPort):
    def __init__(self, usecase: Type[OperationTaxCalculatorPort]) -> None:
        super().__init__()
        self.usecase = usecase()
        self.data: Optional[str] = None

    def input(self) -> None:
        self.data = input()

    def read_input(self) -> Optional[List[OperationTaxDto]]:
        """
        Read Input From StdIn
        """

        if self.data:
            json_data = json.loads(self.data)
            return self.usecase.caculate_tax(
                operations=json_data,
            )

        return None
