"""Flask Application."""
import logging
import sys

from flask import Blueprint, Flask
from flask_apispec.extension import FlaskApiSpec
from flask_cors import CORS
from flask_restful import Api

from db import db

from .config import Config
from .urls import URL_PREFIX, URLS


def create_app():
    # Construct the core app
    app = Flask(__name__)

    # Initialise the flask config
    app.config.from_object(Config())

    logger = logging.getLogger(__name__)
    logger.setLevel(app.config["LOG_LEVEL"])
    app.logger.addHandler(logging.StreamHandler(sys.stdout))

    # Initialise the url routes
    blueprint = Blueprint("api_v1", __name__, url_prefix=URL_PREFIX)

    api = Api(blueprint)

    for cls, url in URLS:
        api.add_resource(cls, url)

    app.register_blueprint(blueprint)

    # Initialise the swagger docs
    docs = FlaskApiSpec(app)

    # Register the swagger docs
    for cls, _ in URLS:
        docs.register(cls, blueprint=blueprint.name)

    # Initialise the database
    db.init_app(app)

    # Initialise CORS support
    CORS(app)

    return app
