from abc import ABC, abstractmethod
from typing import List

from system.application.typings.operation_type import OperationInput


class ReadInputPort(ABC):
    @abstractmethod
    def read_input(self) -> List[List[OperationInput]]:
        """
        Read Input From any kind of input
        """
