from .Model import Model
from .. import db

questions_quizzes_table = db.Table(
    "questions_quizzes",
    db.Column("quiz_id", db.Integer, db.ForeignKey("quizzes.id")),
    db.Column("question_id", db.Integer, db.ForeignKey("questions.id")),
)

quizzes_categories_table = db.Table(
    "quizzes_categories",
    db.Column("category_id", db.Integer, db.ForeignKey("categories.id")),
    db.Column("quizz_id", db.Integer, db.ForeignKey("quizzes.id")),
)


class Quizz(db.Model, Model):
    __tablename__ = 'quizzes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    questions = db.relationship(
        "Question", secondary=questions_quizzes_table
    )


    def to_dict(self):
        return {
            "title": self.title
        }

    def __init__(self, title):
        self.title = title

    @staticmethod
    def get_by_title(title):
        return Quizz.query.filter_by(title=title).first() 
