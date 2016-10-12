from sqlalchemy.orm import defer
import sqlalchemy.exc
# zp
# import zp.config as config
# zp.core
from zp.core.database import db_session
import logger
# zp.models
from zp.models.library import Library
from zp.models.hashes import Hashes


lg = logger.Logger()
lg.setup(__name__)


class Data(object):
    """Library specific data functions wrapper"""
    def __init__(self):
        super(Data, self).__init__()

    @staticmethod
    def add_to_library(data, close=True):
        # library = session.query(Library)
        try:
            item = Library(**data)
            db_session.add(item)
            db_session.commit()
        except sqlalchemy.exc.IntegrityError:
            lg.logger.error("Error inserting item into the database")
            return False
        else:
            return True
        finally:
            if close:
                db_session.remove()

    @staticmethod
    def get_from_library(ufid=False):
        try:
            if ufid:
                Query   = db_session.query(Library).filter(Library.ufid == ufid)
            else:
                Query = db_session.query(Library)
            Query = Query.options(defer('exif_dump'))
        except sqlalchemy.exc.IntegrityError:
            return False
        else:
            data    = []
            for item in Query:
                item = item.__dict__
                data.append(item)
            return data

    @staticmethod
    def add_to_hashes(data, close=True):
        try:
            item = Hashes(**data)
            db_session.add(item)
            db_session.commit()
        except sqlalchemy.exc.IntegrityError:
            return False
        else:
            return True
        finally:
            if close:
                db_session.remove()

    @staticmethod
    def get_from_hashes(ufid=False):
        try:
            if ufid:
                Query = db_session.query(Hashes).filter(Library.ufid == ufid)
            else:
                Query = db_session.query(Hashes)
        except sqlalchemy.exc.IntegrityError:
            return False
        else:
            data = []
            for item in Query:
                item = item.__dict__
                data.append(item)
            return data