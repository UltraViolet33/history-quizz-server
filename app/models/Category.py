from .Model import Model
from .. import db


class Category(db.Model, Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    parent_category_id = db.Column(
        db.Integer, db.ForeignKey("categories.id"), nullable=True
    )
    parent_category = db.relationship(
        "Category", backref=db.backref("children", lazy=True), remote_side=[id]
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "parent_category": self.parent_category.to_dict(),
        }

    def __init__(self, name):
        self.name = name

    def get_by_name(name):
        return Category.query.filter_by(name=name)
