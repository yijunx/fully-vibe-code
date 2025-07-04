from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class ToyBase(BaseModel):
    name: str
    manufacturor: str | None = None
    designer: str | None = None
    number_manufactured: int | None = None

class ToyCreate(ToyBase):
    pass

class Toy(ToyBase):
    id: UUID
    manufacture_time: datetime | None = None
    design_time: datetime | None = None

    class Config:
        orm_mode = True
