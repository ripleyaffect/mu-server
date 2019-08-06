#!/usr/bin/env python3

from flask_script import Manager
from flask_migrate import MigrateCommand

from app import app
from model import migrate

# Create the manager
manager = Manager(app)

# Configure the manager
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
