from sqlalchemy import Column, Integer, String
# zp.core
from zp.core.database import Base

class Library(Base):
    """SQLAlchemy schema for 'relationships' table"""
    __tablename__   = 'relationships'

    id          = Column(Integer, primary_key=True)
    primary     = Column(String(10))
    secondary   = Column(String(10))
    type        = Column(String(1))
    value       = Column(Integer)

    def __init__(self, primary=None, secondary=None, type=None, value=None):
        self.primary    = primary
        self.secondary  = secondary
        self.type       = type
        self.value      = value
