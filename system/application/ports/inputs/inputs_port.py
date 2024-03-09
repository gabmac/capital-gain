from abc import ABC, abstractmethod
from typing import Dict, List, Union


class ReadInputPort(ABC):
    @abstractmethod
    def read_input(self) -> List[List[Dict[str, Union[str, int, float]]]]:
        """
        Read Input From any kind of input
        """
