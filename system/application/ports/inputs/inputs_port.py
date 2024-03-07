from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Union


class ReadInputPort(ABC):
    @abstractmethod
    def read_input(self) -> Optional[List[Dict[str, Union[str, int, float]]]]:
        """
        Read Input From any kind of input
        """
