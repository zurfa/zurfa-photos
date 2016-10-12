# zp.core
from zp.core.image import Image
from zp.core.data import Data
import zp.core.math as math

def make_hash(TYPE,File):
    im = Image()
    if TYPE == 'phash':
        # Generate perception hash
        return im.p_hash(File)
    elif TYPE == 'dhash':
        # Generate difference hash
        return im.d_hash(File)
    elif TYPE == 'whash':
        # Generate wavelet hash
        return im.w_hash(File)
    elif TYPE == 'all':
        # Generate all hashes
        PHASH   = im.p_hash(File)
        DHASH   = im.d_hash(File)
        WHASH   = im.w_hash(File)
        hashes  = {'phash':PHASH, 'dhash':DHASH, 'whash':WHASH}
        return hashes
    else:
        # Invalid hash type specified
        return False

def make_all_hashes():
    libData = Data.get_from_library()

    for item in libData:
        File = item['path']
        hashes = make_hash('all', File)
        if hashes['phash']:
            print "Generated phash for %s%s [%s]" % (item['ufid'],item['extension'],hashes['phash'])
        if hashes['dhash']:
            print "Generated dhash for %s%s [%s]" % (item['ufid'], item['extension'], hashes['dhash'])
        if hashes['whash']:
            print "Generated whash for %s%s [%s]" % (item['ufid'], item['extension'], hashes['whash'])

        hashes.update({'ufid':item['ufid']})
        print Data.add_to_hashes(hashes)def make_hamming():
def make_hamming():
    pass