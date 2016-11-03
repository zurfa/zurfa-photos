from zpl import db, md
import pandas as pd


class Frames(object):

    items = None
    metadata = None
    imports = None


class FrameLoad(object):
    def __init__(self):
        pass


    def load_items(self):
        statement = db.session.query(md.Items).limit(None).statement
        frame = pd.read_sql(statement, db.session.bind)
        Frames.items = frame


    def load_metadata(self):
        statement = db.session.query(md.Metadata).limit(None).statement
        frame = pd.read_sql(statement, db.session.bind)
        Frames.metadata = frame


    def items(self,reload=False):
        if Frames.items is None:
            self.load_items()
            items = Frames.items
        elif reload is True:
            self.load_items()
            items = Frames.items
        else:
            items = Frames.items

        return items


    def metadata(self,reload=False):
        if Frames.metadata is None:
            self.load_metadata()
            items = Frames.metadata
        elif reload is True:
            self.load_metadata()
            items = Frames.metadata
        else:
            items = Frames.metadata

        return items
