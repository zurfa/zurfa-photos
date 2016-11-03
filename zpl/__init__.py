from flask import Flask, send_from_directory, url_for, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy


# Create Flask app
app = Flask(__name__)

# Configure Flask from config
app.config.from_object('zpl.core.config')

# Create SQLAlchemy instance
db = SQLAlchemy(app)

# Import models
# from zpl.core.models import Items, Hashes, Metadata
import zpl.core.models as md

# Import routes
import zpl.web.routes

# Create frame storage
from zpl.core.frames import Frames
