from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Union

from system.application.dto.tax_dto import OperationTaxDto


class OperationTaxCalculatorPort(ABC):
    @abstractmethod
    def caculate_tax(
        self,
        operations: List[Dict[str, Union[str, int, float]]],
    ) -> Optional[List[OperationTaxDto]]:
        """
        Calculate tax given an operation list
        """
