from tests.conftest import BaseConfTest
from tests.operation.fixtures import OperationTaxDTOFixture


class BaseOperationConfTest(BaseConfTest):
    @classmethod
    def setUpClass(cls) -> None:
        cls.operation_tax_fixture = OperationTaxDTOFixture()
