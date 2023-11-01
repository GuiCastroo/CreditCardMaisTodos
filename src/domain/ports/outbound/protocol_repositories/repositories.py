from abc import ABC, abstractmethod


class IGetRepository(ABC):
    @abstractmethod
    async def get_all(self):
        """Get all products with pagination"""

    @abstractmethod
    async def get_by_filter(self, value: str):
        """Get all products with a filter more appropriate with your repository"""


class ICreateRepository(ABC):
    @abstractmethod
    async def create(self, data):
        """Create a new product"""



