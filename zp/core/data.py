from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, defer
import sqlalchemy.exc
# zp
import zp.config as config
# zp.core
import logger
# zp.models
from zp.models.library import Library
from zp.models.library import Hashes



engine  = create_engine('sqlite:///%s' % config.DATABASE, echo=False)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base    = declarative_base()
Base.query = db_session.query_property()

lg = logger.Logger()
lg.setup(__name__)


class Data(object):
    """Library specific data functions wrapper"""
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

    @staticmethod
    def get_from_library():
        try:
            Query   = db_session.query(Library)
            Query   = Query.options(defer('exif_dump'))
        except sqlalchemy.exc.IntegrityError:
            return False
        else:
            data    = []
            for item in Query:
                item = item.__dict__
                data.append(item)
            return data
