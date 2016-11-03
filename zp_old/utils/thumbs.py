import os
# zp
import zp_old.config as config
# zp.core
import zp_old.core.image as image
import zp_old.core.data as data

def make_thumbs(File):
    """Makes all sizes of thumbnails in default directories."""
    # CAUTION! Assumes file exists!
    im = image.Image()
    Im = im.open_image(File)
    file = os.path.split(File)[1]

    LARGE = im.large_thumb(Im, Obj=True)
    MEDIUM = im.medium_thumb(Im, Obj=True)
    SMALL = im.small_thumb(Im, Obj=True)

    im.save_image(LARGE[0], ("%s%s" % (config.DIR_THUMBS_L, file)), LARGE[1])
    im.save_image(MEDIUM[0], ("%s%s" % (config.DIR_THUMBS_M, file)), MEDIUM[1])
    im.save_image(SMALL[0], ("%s%s" % (config.DIR_THUMBS_S, file)), SMALL[1])

    LARGE[0].close()
    MEDIUM[0].close()
    SMALL[0].close()

def make_all_thumbs():
    items = data.Data.get_from_library()
    total=len(items)
    for item in items:
        Index=item['id']
        UFID=item['ufid']
        Image=item['path']
        print "[%s/%s] Making thumbnails for %s" % (Index,total,Image)
        make_thumbs(Image)