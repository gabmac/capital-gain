from abc import ABC, abstractmethod
from typing import List, Optional

from system.application.dto.tax_dto import OperationTaxDto


class ReadInputPort(ABC):
    @abstractmethod
    def read_input(self) -> Optional[List[OperationTaxDto]]:
        """
        Read Input From any kind of input
        """
