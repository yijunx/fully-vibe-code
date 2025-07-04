from sqlalchemy.orm import Session
from app.repositories.toy import ToySqlalchemyRepo
from app.services.toy import ToyService


class ServiceFactory:
    """Factory for creating service instances with proper dependencies."""
    
    def __init__(self, db_session: Session):
        self.db_session = db_session
    
    def create_toy_service(self) -> ToyService:
        """Create a toy service instance."""
        toy_repo = ToySqlalchemyRepo(self.db_session)
        return ToyService(toy_repo) 