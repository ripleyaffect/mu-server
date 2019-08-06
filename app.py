import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


CONFIG_PATH = os.environ.get('CONFIG_PATH', 'config.DevelopmentConfig')


# Create the app
app = Flask(__name__)

# Configure the app
app.config.from_object(CONFIG_PATH)

# Create the db object
db = SQLAlchemy(app)


# Register routes
@app.route('/')
def index():
    return 'Hello world'
