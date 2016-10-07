from sqlalchemy import Column, Integer, String, Numeric, LargeBinary
import time
# zp.core
from zp.core.data import Base


class Library(Base):
    """SQLAlchemy schema for 'library' table"""
    __tablename__   = 'library'

    id          = Column(Integer, primary_key=True)
    ufid        = Column(String(10), unique=True)
    path        = Column(String(128))
    origin      = Column(String(64))
    size        = Column(Integer)
    checksum    = Column(String(40))
    added       = Column(Integer)
    updated     = Column(Integer, default=int(time.time()))
    extension   = Column(String(7))
    format      = Column(String(10))
    category    = Column(String(10))
    taken       = Column(Integer)
    lat         = Column(Numeric(15,11))
    lon         = Column(Numeric(15,11))
    device      = Column(String(32))
    width       = Column(Integer)
    height      = Column(Integer)
    exif_dump   = Column(LargeBinary)