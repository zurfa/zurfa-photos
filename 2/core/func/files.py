import hashlib
import shutil


def sha1_checksum(File ,Object=False):
    """Calculate sha1 checksum on given file."""

    BLOCKSIZE   = 65536
    hasher  = hashlib.sha1()

    try:
        handle  = open(File, 'r')
    except IOError:
        return False
    else:
        with handle as afile:
            buf = afile.read(BLOCKSIZE)
            while len(buf) > 0:
                hasher.update(buf)
                buf = afile.read(BLOCKSIZE)
        checksum    = hasher.hexdigest()
        SHA1    = checksum.upper()
        # self.lg.logger.info("Generated SHA1 checksum for %s" % File)
        return SHA1
    finally:
        handle.close()


def import_file(df):
    file = df.path
    ufid = df.ufid
    ext = df.extension
    origin = df.origin
    library_dest = '/mnt/library/data/library/' + ufid + ext
    origin_dest = '/mnt/library/data/processed' + origin
    df['fl_origin'] = copy_file(file, origin_dest)
    df['fl_lib'] = move_file(file, library_dest)
    # df['fl_origin'] = True
    # df['fl_lib'] = True
    if df['fl_lib']:
        df['path'] = library_dest
    return df

def copy_file(In, Out):
    """Copy file from In path to Out path"""
    try:
        shutil.copy2(In, Out)
    except IOError:
        return False
    except shutil.Error:
        return False
    else:
        return True


def move_file(In, Out):
    """Move file from In path to Out path"""
    try:
        shutil.move(In, Out)
    except IOError:
        return False
    except shutil.Error:
        return False
    else:
        return True