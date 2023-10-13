"""Flask Configuration Definitions."""

from flask_apispec.extension import make_apispec


class Config:
    def __init__(self):
        # Debugging
        self.DEBUG = True
        self.TESTING = False
        self.LOG_LEVEL = "INFO"
        # Databases
        self.SQLALCHEMY_ECHO = True
        self.SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
        # API Spec
        self.APISPEC_SPEC = make_apispec(title="Cakes Project", version="1.0")
        # URI to access API Doc JSON
        self.APISPEC_SWAGGER_URL = "/swagger/"
        # URI to access UI of API Doc
        self.APISPEC_SWAGGER_UI_URL = "/swagger-ui/"
