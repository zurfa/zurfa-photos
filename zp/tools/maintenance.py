from zp import db, app
from zp.core.models import Items, Metadata, Hashes, Thumbs
import zp.core.thumbnail as thumb
import zp.core.config as config


def populate_auxiliary_tables():
    items_table = Items.query.add_columns(Items.ufid).all()
    metadata_table = Metadata.query.add_columns(Metadata.ufid).all()
    hashes_table = Hashes.query.add_columns(Hashes.ufid).all()
    thumbs_table = Thumbs.query.add_columns(Thumbs.ufid).all()

    # items = map(lambda item: dict((i, item.__dict__[i])
    #                                  for i in item.__dict__ if i != '_sa_instance_state'), items_table)
    # metadata = map(lambda item: dict((i,item.__dict__[i])
    #                                  for i in item.__dict__ if i != '_sa_instance_state'), metadata_table)
    # hashes = map(lambda item: dict((i, item.__dict__[i])
    #                                  for i in item.__dict__ if i != '_sa_instance_state'), hashes_table)

    items    = map(lambda item: item[1], items_table)
    metadata = map(lambda item: item[1], metadata_table)
    hashes   = map(lambda item: item[1], hashes_table)
    thumbs   = map(lambda item: item[1], thumbs_table)

    missing = []
    for item in items:
        if not item in metadata:
            missing.append(Metadata(ufid=item))
        if not item in hashes:
            missing.append(Hashes(ufid=item))
        if not item in thumbs:
            missing.append(Thumbs(ufid=item))

    db.session.bulk_save_objects(missing)
    db.session.commit()

