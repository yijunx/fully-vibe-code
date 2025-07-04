from abc import ABC, abstractmethod
from typing import Protocol, TypeVar, Generic

T = TypeVar('T')
CreateT = TypeVar('CreateT')
UpdateT = TypeVar('UpdateT')


class BaseService(ABC, Generic[T, CreateT, UpdateT]):
    """Base service interface for all services."""
    
    @abstractmethod
    def create(self, item_create: CreateT) -> T:
        """Create a new item."""
        pass
    
    @abstractmethod
    def get_by_id(self, item_id) -> T | None:
        """Get an item by its ID."""
        pass
    
    @abstractmethod
    def get_many(self) -> list[T]:
        """Get all items."""
        pass
    
    @abstractmethod
    def update(self, item_id, item_update: UpdateT) -> T | None:
        """Update an item."""
        pass
    
    @abstractmethod
    def delete(self, item_id) -> bool:
        """Delete an item by its ID."""
        pass 