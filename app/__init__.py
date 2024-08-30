from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask
import sqlalchemy as sa
from os import path
import os

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_type=None):
    app = Flask(__name__)

    if config_type == None:
        config_type = os.getenv("CONFIG_TYPE", default="config.DevelopmentConfig")

    app.config.from_object(config_type)

    initialize_extensions(app)
    register_blueprints(app)

    return app


def initialize_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)

    from app.models.Question import Question


def register_blueprints(app):
    from .questions import questions

    app.register_blueprint(questions, url_prefix="/")
