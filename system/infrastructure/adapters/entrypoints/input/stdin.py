import json
from typing import Dict, List, Type, Union

from system.application.ports.inputs.inputs_port import ReadInputPort
from system.application.ports.usecase.operation_tax_calculator_port import (
    OperationTaxCalculatorPort,
)


class ReadStdIn(ReadInputPort):
    def __init__(self, usecase: Type[OperationTaxCalculatorPort]) -> None:
        super().__init__()
        self.usecase = usecase()
        self.data: List[str] = []

    def input(self) -> None:
        while True:
            try:
                line = input()
                if not line:  # exit loop when empty line.
                    break
                self.data.append(line)
            except EOFError:
                break

    def read_input(self) -> List[List[Dict[str, Union[str, int, float]]]]:
        """
        Read Input From StdIn
        """

        data_to_return = []
        for line in self.data:
            line = line.strip()
            line = line.replace("'", '"')
            json_data = json.loads(line)
            data_to_return.append(
                [
                    data.model_dump(mode="json")
                    for data in self.usecase.caculate_tax(
                        operations=json_data,
                    )
                ],
            )
        return data_to_return
