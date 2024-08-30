from .Model import Model
from .. import db


class Question(db.Model, Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(255), nullable=False)

    def __init__(self, text):
        self.text = text