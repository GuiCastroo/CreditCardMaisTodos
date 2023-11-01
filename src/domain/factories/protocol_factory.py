from abc import ABC, abstractmethod
from typing import Any


class Factory(ABC):
    @abstractmethod
    def create(self, data: Any):
        pass
