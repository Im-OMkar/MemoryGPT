from flask import Flask
from config.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from src.routes.user_message import route_gpt, controller_gpt
    app.register_blueprint(route_gpt)
    app.register_blueprint(controller_gpt)

    return app
