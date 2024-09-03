from .Model import Model
from .. import db


class Answer(db.Model, Model):
    __tablename__ = 'answers'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(255), nullable=False)


    def to_dict(self):
        return {
            "text": self.text
        }

    def __init__(self, text):
        self.text = text