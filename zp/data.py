from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric, LargeBinary
from sqlalchemy.orm import scoped_session, sessionmaker
import sqlalchemy.exc
import time
import config
import logger


engine  = create_engine('sqlite:///%s' % config.DATABASE, echo=False)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base    = declarative_base()
Base.query = db_session.query_property()

lg = logger.Logger()
lg.setup(__name__)

class Library(Base):
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

class Hashes(Base):
    __tablename__   = 'hashes'

    id          = Column(Integer, primary_key=True)
    ufid        = Column(String(10), unique=True)
    phash       = Column(String(56))
    dhash       = Column(String(56))
    whash       = Column(String(64))

class Data(object):
    """docstring for Data"""
    def __init__(self):
        super(Data, self).__init__()

    @staticmethod
    def add_to_library(data,Close=True):
        # library = session.query(Library)
        try:
            item    = Library(**data)
            db_session.add(item)
            db_session.commit()
        except sqlalchemy.exc.IntegrityError:
            lg.logger.error("Error inserting item into the database")
            return False
        else:
            return True
        finally:
            if Close:
                db_session.remove()