import os

from api import api_blueprint
from app import app


PORT = os.environ.get('PORT', 7000)


# Register blueprints
app.register_blueprint(api_blueprint)


# Start the app
if __name__ == '__main__':
    app.run(port=PORT)
