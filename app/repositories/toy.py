from uuid import UUID
from sqlalchemy.orm import Session
from datetime import datetime, timezone

from app.models.pydantic.toy import ToyCreate
from app.models.sqlalchemy.toy import ToyRecord


class ToySqlalchemyRepo:
    def __init__(self, rdb: Session):
        self.rdb = rdb

    def create(self, item_create: ToyCreate) -> ToyRecord:
        toy_record = ToyRecord(**item_create.model_dump())
        self.rdb.add(toy_record)
        self.rdb.flush()
        return toy_record

    def get_by_id(self, item_id: UUID) -> ToyRecord | None:
        return self.rdb.query(ToyRecord).filter(ToyRecord.id == item_id).first()

    def get_many(self) -> list[ToyRecord]:
        return self.rdb.query(ToyRecord).all()

    def update_manufacture_status(self, item_id: UUID, number_manufactured: int) -> ToyRecord | None:
        toy_record = self.get_by_id(item_id)
        if toy_record:
            toy_record.manufacture_time = datetime.now(timezone.utc)
            toy_record.number_manufactured = number_manufactured
            self.rdb.flush()
        return toy_record

    def delete(self, item_id: UUID) -> None:
        toy = self.get_by_id(item_id)
        if toy:
            self.rdb.delete(toy)
            self.rdb.flush()
