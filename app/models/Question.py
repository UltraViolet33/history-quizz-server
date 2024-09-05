from .Model import Model
from .. import db

questions_answers_table = db.Table(
    "questions_answers",
    db.Column("answer_id", db.Integer, db.ForeignKey("answers.id")),
    db.Column("question_id", db.Integer, db.ForeignKey("questions.id")),
)

class Question(db.Model, Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(255), nullable=False)
    right_answer_id = db.Column(db.Integer, db.ForeignKey("answers.id"))
    
    right_answer = db.relationship("Answer", backref="questions")
    answers = db.relationship(
        "Answer", secondary=questions_answers_table
    )


    def to_dict(self):
        return {
            "text": self.text,
            "right_answer": self.right_answer.text if self.right_answer else 'No anwer yet',
            "right_answer_id": self.right_answer_id,
        }

    def __init__(self, text, right_answer_id):
        self.text = text
        self.right_answer_id = right_answer_id
