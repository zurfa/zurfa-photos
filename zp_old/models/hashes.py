from sqlalchemy import Column, Integer, String
# zp.core
from zp_old.core.database import Base


class Hashes(Base):
    """SQLAlchemy schema for 'hashes' table"""
    __tablename__   = 'hashes'

    id          = Column(Integer, primary_key=True)
    ufid        = Column(String(10), unique=True)
    phash       = Column(String(56))
    dhash       = Column(String(56))
    whash       = Column(String(64))