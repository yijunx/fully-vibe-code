from uuid import UUID
from typing import List, Optional
from datetime import datetime

from app.models.pydantic.toy import ToyCreate, Toy
from app.models.sqlalchemy.toy import ToyRecord
from app.repositories.toy import ToySqlalchemyRepo
from app.services.base import BaseService


class ToyService(BaseService[Toy, ToyCreate, dict]):
    def __init__(self, toy_repo: ToySqlalchemyRepo):
        self.toy_repo = toy_repo

    def create(self, toy_create: ToyCreate) -> Toy:
        """Create a new toy with the given data."""
        toy_record = self.toy_repo.create(toy_create)
        return Toy.model_validate(toy_record)

    def get_by_id(self, toy_id: UUID) -> Optional[Toy]:
        """Get a toy by its ID."""
        toy_record = self.toy_repo.get_by_id(toy_id)
        if toy_record:
            return Toy.model_validate(toy_record)
        return None

    def get_many(self) -> List[Toy]:
        """Get all toys."""
        toy_records = self.toy_repo.get_many()
        return [Toy.model_validate(record) for record in toy_records]

    def update(self, toy_id: UUID, update_data: dict) -> Optional[Toy]:
        """Update a toy with the given data."""
        toy_record = self.toy_repo.get_by_id(toy_id)
        if not toy_record:
            return None
            
        # Update fields based on the update_data dict
        for field, value in update_data.items():
            if hasattr(toy_record, field):
                setattr(toy_record, field, value)
        
        self.toy_repo.rdb.flush()
        return Toy.model_validate(toy_record)

    def delete(self, toy_id: UUID) -> bool:
        """Delete a toy by its ID."""
        toy_record = self.toy_repo.get_by_id(toy_id)
        if toy_record:
            self.toy_repo.delete(toy_id)
            return True
        return False

    # Additional convenience methods
    def create_toy(self, toy_create: ToyCreate) -> Toy:
        """Create a new toy with the given data."""
        return self.create(toy_create)

    def get_toy(self, toy_id: UUID) -> Optional[Toy]:
        """Get a toy by its ID."""
        return self.get_by_id(toy_id)

    def list_toys(self) -> List[Toy]:
        """Get all toys."""
        return self.get_many()

    def update_manufacture_status(self, toy_id: UUID, number_manufactured: int) -> Optional[Toy]:
        """Update the manufacture status of a toy."""
        toy_record = self.toy_repo.update_manufacture_status(toy_id, number_manufactured)
        if toy_record:
            return Toy.model_validate(toy_record)
        return None

    def update_design_time(self, toy_id: UUID, design_time: datetime) -> Optional[Toy]:
        """Update the design time of a toy."""
        return self.update(toy_id, {"design_time": design_time}) 