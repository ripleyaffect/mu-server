import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

CONFIG_PATH = os.environ.get('CONFIG_PATH', 'config.DevelopmentConfig')
PORT = os.environ.get('PORT', 7000)


# Create the app
app = Flask(__name__)

# Configure the app
app.config.from_object(CONFIG_PATH)

# Create the db object
db = SQLAlchemy(app)


@app.route('/')
def index():
    return 'Hello world'


if __name__ == '__main__':
    app.run(port=PORT)
