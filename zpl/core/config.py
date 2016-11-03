from zpl import app


# SQLAlchemy
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + app.root_path + '/app.db'
# SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_DATABASE_URI = 'mysql://zpl:1234@localhost/zpl'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO=True

# Flask
DEBUG = True
SERVER_NAME = None
ASSETS_DEBUG = True