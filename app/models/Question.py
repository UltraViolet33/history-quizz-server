from .Model import Model
from .. import db


questions_categories_table = db.Table(
    "questions_categories",
    db.Column("category_id", db.Integer, db.ForeignKey("categories.id")),
    db.Column("question_id", db.Integer, db.ForeignKey("questions.id")),
)

class Question(db.Model, Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(255), nullable=False)
    right_answer_id = db.Column(db.Integer, db.ForeignKey("answers.id"))
    
    right_answer = db.relationship("Answer", backref="questions")
    categories = db.relationship(
        "Category", secondary=questions_categories_table, backref="questions"
    )


    def to_dict(self):
        return {
            "text": self.text,
            "right_answer": self.right_answer.text if self.right_answer else 'No anwer yet'
        }

    def __init__(self, text, right_answer_id):
        self.text = text
        self.right_answer_id = right_answer_id
