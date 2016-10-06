import zp.logger as logger
import zp.importer as importer
import zp.exif as exif
import zp.files as files
import zp.config as config
import zp.exp as exp
import zp.image as image
import zp.data as data


import os
import time
import Queue


lg = logger.Logger()
lg.setup(__name__)


def import_directory(Dir=False):
    fi = files.Files()
    if Dir:
        Directory = Dir
    else:
        Directory = config.DIR_IMPORT
        lg.logger.warning("No import directory specified, using default")

    try:
        # Try to find valid files
        Files = fi.get_imports(Directory)
    except OSError as Err:
        return False
    except exp.DirectoryError as Err:
        return False
    except exp.ValidFilesError as Err:
        return False
    except exp.NullDirectoryError as Err:
        return False
    else:
        # Successfully recieved atleast one valid file
        try:
            Session = fi.import_session_create()
        except OSError:
            # Unable to create import session directory
            lg.logger.critical(
                "Could not create import session directory, can not continue.")
            return False
        else:
            # Import session directory created
            lg.logger.info("Importing files...")
            NumFiles = len(Files)
            bad_files = []
            for Index, File in enumerate(Files, 1):
                lg.logger.info("Importing file %s/%s %s" %
                               (Index, NumFiles, File))
                imported = import_file(File, Session)
                if not imported:
                    lg.logger.warning("Error while importing %s" % File)
                    bad_files.append(File)
                else:
                    # Make thumbnails
                    make_thumbs(imported['path'])
            if len(bad_files) > 0:
                for file in bad_files:
                    lg.logger.warning("Unable to import %s" % file)
            lg.logger.info("Finished importing files")


def import_file(File, Export=False, Options=None):
    """Import a single file to the library"""
    fi = files.Files()
    imp = importer.Importer()
    ex = exif.Exif()
    im = image.Image()
    dt = data.Data()

    try:
        os.stat(File)
        width, height, imformat = im.is_image(File)
    except OSError:
        # File doesn't exist or isn't readable
        lg.logger.error("Unable to read file %s " % File)
        return False
    except IOError:
        # Is not a valid image file
        # lg.logger.error("File does not appear to be a valid image %s " % File)
        return False
    else:
        if not Export:
            Export = "%simport/" % config.DIR_PROCESSED

        Data = {}
        # Generate EXIF data
        EXIF = ex.exif_tags(File,True)
        if EXIF:
            Data.update(EXIF)
        else:
            lg.logger.warning("No EXIF data found in %s " % File)
        # Generate sha1 checksum
        SHA1 = fi.sha1_checksum(File)
        if SHA1:
            Data.update({'checksum': SHA1})
        # Generate paths and UFID
        UFID = imp.new_ufid()
        if UFID:
            Data.update({'ufid': UFID})
        # Generate paths
        ORIG = os.path.split(File)[1]
        EXT  = os.path.splitext(File)[1]
        if UFID:
            DEST = "%s%s%s" % (config.DIR_LIBRARY, UFID,
                               EXT)
            Data.update({'path': DEST, 'origin': ORIG, 'extension': EXT})
        # Generate timestamp
        Data.update({'added': int(time.time())})
        # Get filesize
        Data.update({'size': os.path.getsize(File)})
        # Get dimensions
        Data.update({'width':width,'height':height})
        # Get format
        Data.update({'format':imformat})

        if 'ufid' in Data and 'path' in Data:
            try:
                os.stat(DEST)
            except OSError:
                EXISTS = False
            else:
                EXISTS = True
                return False

            if not EXISTS:
                # Destination file does not already exist
                if fi.copy_file(File, DEST):
                    # Successfully copied file to library
                    if os.path.isdir(Export):
                        # Export directory is a valid directory
                        if fi.move_file(File, Export):
                            # Successfully moved original file to processed
                            dt.add_to_library(Data)
                            return Data
                        else:
                            # Unable to move original file to processed files
                            return False
                    else:
                        # Export directory is not a valid directory
                        return False
                else:
                    # Unable to copy file to library
                    return False
            else:
                # Destination file already exists
                return False
        else:
            return False


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
