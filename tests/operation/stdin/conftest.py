from unittest.mock import patch

from tests.conftest import BaseStdinConfTest
from tests.operation.conftest import BaseOperationConfTest

from system.application.usecase.operation_tax_calculator import (
    OperationTaxCalculatorUseCase,
)
from system.infrastructure.adapters.entrypoints.input.stdin import ReadStdIn


class OperationStdinConfTest(BaseOperationConfTest, BaseStdinConfTest):
    @classmethod
    def setUpClass(cls) -> None:
        cls.input_handler = ReadStdIn(
            usecase=OperationTaxCalculatorUseCase,
        )
        cls.patch_use_case = patch.object(
            OperationTaxCalculatorUseCase,
            "caculate_tax",
        )
        cls.patch_input = patch.object(
            ReadStdIn,
            "_input",
        )
        cls.patch_use_case.start()
        cls.patch_input.start()
        return super().setUpClass()

    def tearDown(self) -> None:
        self.patch_use_case.stop()
        self.patch_input.stop()
        return super().tearDown()
