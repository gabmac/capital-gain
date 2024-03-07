from system.application.usecase.operation_tax_calculator import (
    OperationTaxCalculatorUseCase,
)
from system.infrastructure.adapters.entrypoints.input.stdin import ReadStdIn

if __name__ == "__main__":
    handler = ReadStdIn(
        usecase=OperationTaxCalculatorUseCase,
    )
    handler.input()
    data = handler.read_input()
    print(
        data,
    )
