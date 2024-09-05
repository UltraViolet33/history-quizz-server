from .Model import Model
from .. import db

questions_quizzes_table = db.Table(
    "questions_quizzes",
    db.Column("quiz_id", db.Integer, db.ForeignKey("quizzes.id")),
    db.Column("question_id", db.Integer, db.ForeignKey("questions.id")),
)


class Quizz(db.Model, Model):
    __tablename__ = "quizzes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    questions = db.relationship("Question", secondary=questions_quizzes_table)

    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=True)
    category = db.relationship(
        "Category",
        backref=db.backref("quizzes", lazy=True),
    )

    def to_dict(self):
        return {"title": self.title}

    def __init__(self, title):
        self.title = title

    @staticmethod
    def get_by_title(title):
        return Quizz.query.filter_by(title=title).first()
