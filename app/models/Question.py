from .Model import Model
from .. import db


class Question(db.Model, Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(255), nullable=False)
    right_answer = db.Column(db.Integer, db.ForeignKey(
        "answers.id"))


    def to_dict(self):
        return {
            "text": self.text
        }

    def __init__(self, text, right_answer):
        self.text = text
        self.right_answer = right_answer