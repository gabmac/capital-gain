from abc import ABC, abstractmethod
from typing import List

from system.application.dto.tax_dto import OperationTaxDto
from system.application.typings.operation_type import OperationInput


class OperationTaxCalculatorPort(ABC):
    @abstractmethod
    def caculate_tax(
        self,
        operations: List[OperationInput],
    ) -> List[OperationTaxDto]:
        """
        Calculate tax given an operation list
        """
