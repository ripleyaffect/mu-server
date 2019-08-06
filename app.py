import os

from flask import Flask

CONFIG_PATH = os.environ.get('CONFIG_PATH', 'config.DevelopmentConfig')
PORT = os.environ.get('PORT', 7000)

app = Flask(__name__)

app.config.from_object(CONFIG_PATH)

@app.route('/')
def index():
    return 'Hello world'

if __name__ == '__main__':
    app.run(port=PORT)
