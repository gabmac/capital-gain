import json

from tests.operation.stdin.conftest import OperationStdinConfTest


class TestOperationStdIn(OperationStdinConfTest):
    def setUp(self) -> None:
        self.patch_use_case.target.caculate_tax.return_value = [
            self.operation_tax_fixture.mock_buy_tax_value,
        ]
        return super().setUp()

    def test_operation_stdin(self) -> None:
        data_str = json.dumps(
            [
                self.operation_tax_fixture.entity_fixture_buy.mock_operation.model_dump(
                    exclude="tax",
                    mode="json",
                ),
            ],
        )
        self.input_handler.data = [data_str]
        result = self.input_handler.read_input()
        self.assertEqual(
            result,
            [[self.operation_tax_fixture.mock_buy_tax_value.model_dump()]],
        )
        self.patch_use_case.target.caculate_tax.assert_called_once_with(
            operations=[
                self.operation_tax_fixture.entity_fixture_buy.mock_operation.model_dump(
                    exclude="tax",
                    mode="json",
                ),
            ],
        )
