from tests.usecase.contest import OperationUseCaseConfTest


class OperationTaxCalculatorTest(OperationUseCaseConfTest):
    def test_buy_operation_tax(self) -> None:
        results = self.tax_calculator_usecase.caculate_tax(
            operations=[
                self.operation_tax_fixture.entity_fixture_buy.mock_operation.model_json_schema(
                    mode="json",
                ),
            ],
        )
        for result in results:
            self.assertEqual(self.operation_tax_fixture.mock_buy_tax_value, result)
            self.assertEqual(self.operation_tax_fixture.mock_buy_tax_value.tax, 0)

    def test_sell_operation_not_reached_threshold(self) -> None:
        results = self.tax_calculator_usecase.caculate_tax(
            operations=[
                self.operation_tax_fixture.entity_fixture_sell.mock_operation.model_json_schema(
                    mode="json",
                ),
            ],
        )
        for result in results:
            self.assertEqual(self.operation_tax_fixture.mock_sell_tax_value, result)
            self.assertEqual(result.tax, 0)

    def test_sell_operation_with_loss(self) -> None:
        results = self.tax_calculator_usecase.caculate_tax(
            operations=[
                operation.model_json_schema(mode="json")
                for operation in self.operation_tax_fixture.entity_fixture_buy.mock_sell_with_loss
            ],
        )
        self.assertEqual(self.operation_tax_fixture.mock_sell_with_loss, results)
        for result in results:
            self.assertEqual(result, 0)

        self.assertGreater(self.tax_calculator_usecase.loss, 0)

    def test_sell_operation_with_profit(self) -> None:
        results = self.tax_calculator_usecase.caculate_tax(
            operations=[
                operation.model_json_schema(mode="json")
                for operation in self.operation_tax_fixture.entity_fixture_buy.mock_sell_with_profit
            ],
        )
        self.assertEqual(self.operation_tax_fixture.mock_sell_with_loss, results)

        self.assertEqual(self.tax_calculator_usecase.loss, 0)
