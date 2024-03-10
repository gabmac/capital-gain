import json
from typing import List, Type

from system.application.ports.inputs.inputs_port import ReadInputPort
from system.application.ports.usecase.operation_tax_calculator_port import (
    OperationTaxCalculatorPort,
)
from system.application.typings.operation_type import OperationInput


class ReadStdIn(ReadInputPort):
    def __init__(self, usecase: Type[OperationTaxCalculatorPort]) -> None:
        super().__init__()
        self.usecase = usecase
        self.data: List[str] = []

    def _input(self) -> None:
        while True:
            try:
                line = input()
                line = line.strip()
                if not line:  # exit loop when empty line.
                    break
                self.data.append(line)
            except EOFError:
                break

    def read_input(self) -> List[List[OperationInput]]:
        """
        Read Input From StdIn
        """

        self._input()

        data_to_return = []
        for line in self.data:
            line = line.replace("'", '"')
            json_data = json.loads(line)
            run_usecase = self.usecase()
            data_to_return.append(
                [
                    data.model_dump(mode="json")
                    for data in run_usecase.caculate_tax(
                        operations=json_data,
                    )
                ],
            )
        return data_to_return
