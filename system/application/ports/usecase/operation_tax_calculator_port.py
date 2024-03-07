from abc import ABC, abstractmethod
from typing import Dict, List, Union

from system.application.dto.tax_dto import OperationTaxDto


class OperationTaxCalculatorPort(ABC):
    @abstractmethod
    def caculate_tax(
        self,
        operation: List[Dict[str, Union[str, int, float]]],
    ) -> OperationTaxDto:
        """
        Calculate tax given an operation list
        """
