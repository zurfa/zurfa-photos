from zp import app


# SQLAlchemy
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + app.root_path + '/app.db'
# SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_DATABASE_URI = 'mysql://zpl:1234@localhost/zpl'
SQLALCHEMY_TRACK_MODIFICATIONS = False
# SQLALCHEMY_ECHO=True

# Flask
DEBUG = True
SERVER_NAME = None
ASSETS_DEBUG = True

# Directories
FILES_ROOT = '/mnt/library/data/'
IMPORT_DIR = FILES_ROOT + 'import/'
LIBRARY_DIR = FILES_ROOT + 'library/'
PROCESSED_DIR = FILES_ROOT + 'processed/'
THUMBS_DIR = FILES_ROOT + 'thumbs/'
THUMBS_LARGE_DIR = THUMBS_DIR + 'large/'
THUMBS_MEDIUM_DIR = THUMBS_DIR + 'medium/'
THUMBS_SMALL_DIR = THUMBS_DIR + 'small/'
THUMBS_SQUARE_DIR = THUMBS_DIR + 'square/'

# Miscellaneous
VALID_EXTENSIONS = ['.jpg', '.jpeg']
UFID_LENGTH = 10
DIR_PROC_FORMAT	= "import_%Y%m%d_%H%M%S/"

# Hashes
PHASH_SIZE	= 15
DHASH_SIZE	= 15
WHASH_SIZE  = 16

# Thumbnails
LARGE_THUMB_SIZE		= 500
MEDIUM_THUMB_SIZE		= 250
SMALL_THUMB_SIZE		= 100
SQUARE_THUMB_SIZE       = 250
LARGE_THUMB_QUALITY		= 95
MEDIUM_THUMB_QUALITY	= 80
SMALL_THUMB_QUALITY		= 20
SQUARE_THUMB_QUALITY    = 20