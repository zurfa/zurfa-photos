import zp.core.config as config
import string, random, shutil, os, time
from zp.core.models import Items, Metadata, Hashes
from zp import app, db


def ls(dir):
    try:
        files = os.listdir(dir)
    except OSError:
        return []
    else:
        return files


def get_imports(dir=None, stat=False):
    """Generates list of files in specified

    Keyword arguments:
        dir  -- directory to import, uses config default if not specified
        stat -- get file sizes with list of files if True
        """
    valid_ext = config.VALID_EXTENSIONS

    # If dir is not specified, use config default
    if not dir:
        dir = config.IMPORT_DIR

    # Get list of files in dir
    files = ls(dir)

    # Is there any files in dir?
    if len(files) == 0:
        print 'Unable to find any files in dir'
        return False

    # Filter files with valid extensions
    valid = []
    for file in files:
        ext = os.path.splitext(file)[1]
        if ext in valid_ext:
            file = dir + file
            if stat:
                size = os.stat(file).st_size
            else:
                size = None
            item = {'path':file,'size':size}
            valid.append(item)

    # Is there any valid files in dir?
    if len(valid) == 0:
        print 'Unable to find any valid files in dir'
        return False

    # Return list of files with sizes
    return valid


def import_files(list, session=False):
    """Run import on a list of files"""
    # Create session directory (if session is True)
    if session:
        session_dir = create_session_directory()
    running = True
    imports = []
    try:
        for item in list:
            path = item['path']
            size = item['size']
            if session:
                orm = import_file(path, move=True, session=session_dir)
            else:
                orm = import_file(path)
            imports.append(orm)
            if len(imports) >= 100:
                bulk_library_insert(imports)
                imports = []
            if not running:
                # exit('User exited')
                print 'User exited'
                break
    except KeyboardInterrupt:
        running = False

    if len(imports) > 0:
        bulk_library_insert(imports)
        imports = []

    return True


def import_file(file, move=False, session=None):
    """Import a single file to the library

    Keyword arguments:
        move    -- If True, will move original file processed directory
        session -- Session directory to move processed files to (move must be True)

    item table:
        ufid       VARCHAR(10)  Unique identifier
        status     INTEGER(1)   Status of file in library
        path       VARCHAR(256) Absolute path of file in library
        origin     VARCHAR(64)  Original name of file
        size       INTEGER(12)  Size of file
        added      INTEGER(10)  Timestamp (in seconds) of when file was added
        updated    INTEGER(10)  Timestamp (in seconds) of when item was modified
        extension  VARCHAR(8)   Extension of file
        category   VARCHAR(10)  Category of file
    """
    # Preliminary data
    print file
    ufid = generate_ufid()
    origin = os.path.split(file)[1]
    size = os.stat(file).st_size
    added = time.time()
    extension = os.path.splitext(file)[1]

    # Copy file to library
    new_file = config.LIBRARY_DIR + ufid + extension
    try:
        shutil.copy2(file, new_file)
    except IOError:
        status = -1
    except shutil.Error:
        status = 0
    else:
        status = 1

    # Move processed file
    if move:
        try:
            if session:
                processed_file = session + origin
                shutil.move(file, processed_file)
            else:
                exit('Session directory is invalid')
        except IOError:
            pass
        except shutil.Error:
            pass
        else:
            pass

    # Build ORM item for file
    item = Items(ufid=ufid, status=status, path=new_file, origin=origin, size=size, added=added, extension=extension)

    return item


def generate_ufid(chars=string.ascii_uppercase + string.digits, exists=False):
    gen_ufid = lambda: ''.join(random.choice(chars) for _ in range(config.UFID_LENGTH))
    if exists:
        ufid = gen_ufid()
        num = Items.query.filter(Items.ufid == ufid)
        return ufid
    else:
        ufid = gen_ufid()
        return ufid


def bulk_library_insert(items):
    db.session.bulk_save_objects(items)
    db.session.commit()


def create_session_directory():
    """Creates a datestamp unique directory for processed files"""
    # Build session directory name
    time_struct = time.gmtime(time.time())
    timestamp = time.strftime(config.DIR_PROC_FORMAT, time_struct)
    export = "%s%s" % (config.PROCESSED_DIR, timestamp)

    # Create session directory
    try:
        os.mkdir(export)
    except OSError:
        return OSError
    print "Created session directory: %s" % export
    return export