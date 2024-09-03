from flask_sqlalchemy import SQLAlchemy
from flask_crud_generator import CRUDGenerator
from flask_migrate import Migrate
from flask import Flask
import os

db = SQLAlchemy()
migrate = Migrate()
crud = CRUDGenerator()


def create_app(config_type=None):
    app = Flask(__name__)

    if config_type == None:
        config_type = os.getenv("CONFIG_TYPE", default="config.DevelopmentConfig")

    app.config.from_object(config_type)

    initialize_extensions(app)
    return app


def initialize_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    crud.init_app(app, db)

    from app.models.Question import Question
    from app.models.Answer import Answer
    from app.models.Category import Category


    from .questions import questions

    crud.generate_web_routes(Question, questions, 'questions')
    crud.generate_web_routes(Answer)
    crud.generate_web_routes(Category)


