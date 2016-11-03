from zpl import db
import time


# SELECT uid,
#        ufid,
#        path,
#        origin,
#        size,
#        added,
#        updated,
#        extension,
#        format,
#        category
#   FROM items;

class Items(db.Model):
    """SQLAlchemy schema for 'items' table"""
    __tablename__   = 'items'

    uid         = db.Column(db.Integer, primary_key=True)
    ufid        = db.Column(db.String(10), unique=True)
    status      = db.Column(db.Boolean, index=True)
    path        = db.Column(db.String(128))
    origin      = db.Column(db.String(64))
    size        = db.Column(db.Integer)
    added       = db.Column(db.Integer)
    updated     = db.Column(db.Integer, default=int(time.time()))
    extension   = db.Column(db.String(7))
    category    = db.Column(db.String(10))

    def __init__(self, ufid=None):
        self.ufid = ufid


class Metadata(db.Model):
    """SQLAlchemy schema for 'metadata' table"""
    __tablename__   = 'metadata'

    # uid         = db.Column(db.Integer, primary_key=True)
    ufid        = db.Column(db.String(10), primary_key=True, unique=True)
    format      = db.Column(db.String(16))
    width       = db.Column(db.Integer)
    height      = db.Column(db.Integer)
    checksum    = db.Column(db.String(40))
    taken       = db.Column(db.Integer)
    lat         = db.Column(db.Numeric(15,11))
    lon         = db.Column(db.Numeric(15,11))
    device      = db.Column(db.String(32))
    dump        = db.Column(db.LargeBinary)


class Hashes(db.Model):
    """SQLAlchemy schema for 'hashes' table"""
    __tablename__   = 'hashes'

    uid         = db.Column(db.Integer, primary_key=True)
    ufid        = db.Column(db.String(10), unique=True)
    phash       = db.Column(db.String(56))
    dhash       = db.Column(db.String(56))
    whash       = db.Column(db.String(64))


    def __init__(self, ufid=None):
        self.ufid = ufid