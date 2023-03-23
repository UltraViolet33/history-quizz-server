from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import os
import sqlalchemy as sa


db = SQLAlchemy()


def create_app(config_type=None):
    app = Flask(__name__)

    if config_type == None:
        config_type = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')

    app.config.from_object(config_type)

    initialize_extensions(app)
    register_blueprints(app)

    engine = sa.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    inspector = sa.inspect(engine)
    # if not inspector.has_table("users") or not inspector.has_table("movies"):
    # with app.app_context():
    #     db.drop_all()
    #     db.create_all()

    # app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

    return app


def initialize_extensions(app):
    db.init_app(app)

    # from app.models.User import User
    # from app.models.Movie import Movie
    # from app.models.Category import Category


def register_blueprints(app):
    pass
    # from .auth import auth
    # from .movies import movies
    # app.register_blueprint(auth, url_prefix="/")
    # app.register_blueprint(movies, url_prefix="/")