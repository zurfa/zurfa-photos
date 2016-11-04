from zp import db
import time


class Items(db.Model):
    """SQLAlchemy schema for 'items' table"""
    __tablename__   = 'items'

    uid         = db.Column(db.Integer, primary_key=True)
    ufid        = db.Column(db.String(10), unique=True)
    status      = db.Column(db.Boolean, index=True)
    path        = db.Column(db.String(128))
    origin      = db.Column(db.String(64))
    size        = db.Column(db.Integer)
    added       = db.Column(db.Integer, default=int(time.time()))
    updated     = db.Column(db.Integer)
    extension   = db.Column(db.String(7))
    category    = db.Column(db.String(10))

    def __init__(self, uid=None, ufid=None, status=None, path=None, origin=None,
                 size=None, added=None, updated=None, extension=None, category=None):
        self.uid = uid
        self.ufid = ufid
        self.status = status
        self.path = path
        self.origin = origin
        self.size = size
        self.added = added
        self.updated = updated
        self.extension = extension
        self.category = category



class Metadata(db.Model):
    """SQLAlchemy schema for 'metadata' table"""
    __tablename__   = 'metadata'

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


    # billing_address_id = Column(Integer, ForeignKey("address.id"))
    # shipping_address_id = Column(Integer, ForeignKey("address.id"))
    #
    # billing_address = relationship("Address", foreign_keys=[billing_address_id])
    # shipping_address = relationship("Address", foreign_keys=[shipping_address_id])



class Hashes(db.Model):
    """SQLAlchemy schema for 'hashes' table"""
    __tablename__   = 'hashes'

    ufid        = db.Column(db.String(10), primary_key=True, unique=True)
    checksum    = db.Column(db.String(40))
    phash       = db.Column(db.String(56))
    dhash       = db.Column(db.String(56))
    whash       = db.Column(db.String(64))


    def __init__(self, ufid=None):
        self.ufid = ufid


class Thumbs(db.Model):
    """SQLAlchemy schema for 'thumbnails' table"""
    __tablename__   = 'thumbnails'

    ufid        = db.Column(db.String(10), primary_key=True, unique=True)
    large       = db.Column(db.Boolean)
    medium      = db.Column(db.Boolean)
    small       = db.Column(db.Boolean)
    square      = db.Column(db.Boolean)


    def __init__(self, ufid=None, large=None, medium=None, small=None, square=None):
        self.ufid = ufid
        self.large = large
        self.medium = medium
        self.small = small
        self.square = square