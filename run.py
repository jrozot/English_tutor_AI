# run.py

from flask import Flask
from app.routes import routes

def create_app():
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False  # Ensure UTF-8 for accented chars
    app.register_blueprint(routes)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='127.0.0.1', port=5000, debug=True)
