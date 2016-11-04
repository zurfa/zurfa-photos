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

def make_missing_thumbs():
    thumbs_table = Thumbs.query.all()

    missing = []
    for item in thumbs_table:
        print "%s %s %s %s %s" % (item.ufid,item.large,item.medium,item.small,item.square)
        values = [item.large, item.medium, item.small, item.square]
        if False in values:
            missing.append({'ufid': item.ufid, 'values': values})

    missing_buffer = []
    for item in missing:
        missing_buffer.append(make_missing_thumb(item))
        if len(missing_buffer) > 10:
            print 'Updating mappings'
            db.session.bulk_update_mappings(Thumbs, missing_buffer)
            db.session.commit()
            missing_buffer = []
    if len(missing_buffer) > 0:
        db.session.bulk_update_mappings(Thumbs, missing_buffer)
        db.session.commit()


def make_missing_thumb(titem):
    """Generates thumbnails for an image
    Expects a dict with keys ufid and values
    Values is a list of booleans
    [large, medium, small, square]
    """
    ufid = titem['ufid']
    vlarge, vmedium, vsmall, vsquare = titem['values']
    item = Items.query.filter(Items.ufid==ufid).first()
    path = item.path
    ext = item.extension
    img = thumb.open_image(path)
    thumbs = {'ufid':ufid}

    if not vlarge:
        thumb_path = config.THUMBS_LARGE_DIR + ufid + ext
        thumb_large, options = thumb.large_thumb(img)
        ts = thumb.save_image(thumb_large, thumb_path, options)
        thumb_large.close()
        print "%s: Created large thumb" % ufid
        if ts:
            thumbs.update({'large':True})
    if not vmedium:
        thumb_path = config.THUMBS_MEDIUM_DIR + ufid + ext
        thumb_medium, options = thumb.medium_thumb(img)
        ts = thumb.save_image(thumb_medium, thumb_path, options)
        thumb_medium.close()
        print "%s: Created medium thumb" % ufid
        if ts:
            thumbs.update({'medium':True})
    if not vsmall:
        thumb_path = config.THUMBS_SMALL_DIR + ufid + ext
        thumb_small, options = thumb.small_thumb(img)
        ts = thumb.save_image(thumb_small, thumb_path, options)
        thumb_small.close()
        print "%s: Created small thumb" % ufid
        if ts:
            thumbs.update({'small':True})
    if not vsquare:
        thumb_path = config.THUMBS_SQUARE_DIR + ufid + ext
        thumb_square, options = thumb.square_thumb(img)
        ts = thumb.save_image(thumb_square, thumb_path, options)
        thumb_square.close()
        print "%s: Created square thumb" % ufid
        if ts:
            thumbs.update({'square':True})

    img.close()
    return thumbs