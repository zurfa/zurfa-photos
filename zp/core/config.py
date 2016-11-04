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

# Miscellaneous settings
VALID_EXTENSIONS = ['.jpg', '.jpeg']
UFID_LENGTH = 10
DIR_PROC_FORMAT	= "import_%Y%m%d_%H%M%S/"