from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
import uuid
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class ToyRecord(Base):
    __tablename__ = 'toys'

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String, index=True)
    manufacture_time: Mapped[datetime | None] = mapped_column(DateTime)
    manufacturor: Mapped[str] = mapped_column(String)
    design_time: Mapped[datetime | None] = mapped_column(DateTime)
    designer: Mapped[str] = mapped_column(String)
    number_manufactured: Mapped[int] = mapped_column(Integer)
