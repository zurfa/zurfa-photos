from PIL import Image, ImageDraw, JpegImagePlugin as PIL
# zp
import zp.core.config as config
# zp.core
import imagehash


def image_constraints(wh, max):
    """returns new image size constraints based on max."""
    Width, Height   = wh
    Ratio   = float(Width)/float(Height)

    if Width > Height:
        Size    = (max,int(max/Ratio))
        return Size
    elif Width < Height:
        Size    = (int(max*Ratio),max)
        return Size
    else:
        Size    = (max,max)
        return Size


def large_thumb(img):
    # Set additional options
    Options = {}
    Options['quality'] = config.LARGE_THUMB_QUALITY
    Options['optimize'] = True
    Options['qtables'] = 'web_high'

    if img:
        Size = image_constraints(img.size, config.LARGE_THUMB_SIZE)
        Image = img.resize(Size, resample=PIL.Image.BILINEAR)
        return (Image, Options)
    else:
        return False


def medium_thumb(img):
    # Set additional options
    Options = {}
    Options['quality'] = config.MEDIUM_THUMB_QUALITY
    Options['optimize'] = True
    Options['qtables'] = 'web_high'

    if img:
        Size = image_constraints(img.size, config.MEDIUM_THUMB_SIZE)
        Image = img.resize(Size, resample=PIL.Image.BILINEAR)
        return (Image, Options)
    else:
        return False


def small_thumb(img):
    # Set additional options
    Options = {}
    Options['quality'] = config.SMALL_THUMB_QUALITY
    Options['optimize'] = True
    Options['qtables'] = 'web_low'

    if img:
        Size = image_constraints(img.size, config.SMALL_THUMB_SIZE)
        Image = img.resize(Size, resample=PIL.Image.BILINEAR)
        return (Image, Options)
    else:
        return False


def square_thumb(img):
    """makes a square thumb cropped from center."""
    # Set additional options
    options = {}
    options['quality'] = config.SQUARE_THUMB_QUALITY
    options['optimize'] = True
    options['qtables'] = 'web_high'

    def polybox(xy):
        xy = (xy[0] - 1, xy[1] - 1)
        ratio = float(xy[0]) / float(xy[1])
        # center	= ((xy[0]/2),(xy[1]/2))
        if ratio >= 1:
            # Width is greater than height
            polybox = [
                ((xy[0] - xy[1]) / 2, 0),
                ((xy[0] + xy[1]) / 2, xy[1])
            ]
        elif ratio <= 1:
            # Width is less than height
            polybox = [
                (0, (xy[1] - xy[0]) / 2),
                (xy[0], (xy[1] + xy[0]) / 2)
            ]

        # print "%s %s" %(xy,polybox)
        return polybox

    size = config.SQUARE_THUMB_SIZE
    polybox = polybox(img.size)
    img = img.crop(
        (
            polybox[0][0],
            polybox[0][1],
            polybox[1][0],
            polybox[1][1]
        )
    )
    img = img.resize((size, size))
    return (img, options)


def open_image(file):
    try:
        img = PIL.Image.open(file)
    except IOError:
        return False
    else:
        return img


def save_image(img, dest, options=None):
    try:
        if options:
            img.save(dest, **options)
        else:
            img.save(dest)
    except IOError:
        return False
    else:
        return True