import hashlib
import shutil


def sha1_checksum(File ,Object=False):
    """Calculate sha1 checksum on given file."""

    BLOCKSIZE   = 65536
    hasher  = hashlib.sha1()

    try:
        handle  = open(File.path, 'r')
    except IOError:
        return None
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
        if 'handle' in locals():
            handle.close()