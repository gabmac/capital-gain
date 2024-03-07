from tests.conftest import BaseUseCaseConfTest
from tests.operation.conftest import BaseOperationConfTest
from tests.operation.fixtures import OperationTaxDTOFixture

from system.application.usecase.operation_tax_calculator import (
    OperationTaxCalculatorUseCase,
)


class OperationUseCaseConfTest(BaseUseCaseConfTest, BaseOperationConfTest):
    @classmethod
    def setUpClass(cls) -> None:
        cls.operation_tax_fixture = OperationTaxDTOFixture()
        return super().setUp()

    def setUp(self) -> None:
        self.tax_calculator_usecase = OperationTaxCalculatorUseCase()
        return super().setUp()
