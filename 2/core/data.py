from zpl import db, Items, Metadata
import zpl.core.func.imports as imp
import pandas as pd

class Load(object):
    def __init__(self):
        pass

    @staticmethod
    def load_items():
        try:
            statement = db.session.query(Items).limit(None).statement
            frame = pd.read_sql(statement, db.session.bind)
        except:
            return False
        else:
            Frames.items = frame
            return True

    @staticmethod
    def load_metadata():
        try:
            statement = db.session.query(Metadata).limit(None).statement
            frame = pd.read_sql(statement, db.session.bind)
        except:
            return False
        else:
            Frames.metadata = frame
            return True


class Frames(object):
    # def __init__(self):
    #     Load.load_items()
    #     Generate.gen_imports()

    items = None
    metadata = None
    # imports = None


class Data(object):
    @staticmethod
    def Items(reload=False):
        if Frames.items is None:
            Load.load_items()
            items = Frames.items
        elif reload is True:
            Load.load_items()
            items = Frames.items
        else:
            items = Frames.items

        return items

    @staticmethod
    def Metadata(reload=False):
        if Frames.metadata is None:
            Load.load_metadata()
            items = Frames.metadata
        elif reload is True:
            Load.load_metadata()
            items = Frames.metadata
        else:
            items = Frames.metadata

        return items