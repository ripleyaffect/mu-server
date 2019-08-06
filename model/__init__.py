from flask_migrate import Migrate

from app import app, db

# Import all the models
from .task import Task
from .user import User


# Create the migrate object
migrate = Migrate(app, db)
