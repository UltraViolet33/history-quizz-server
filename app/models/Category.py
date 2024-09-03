from .Model import Model
from .. import db



class Category(db.Model, Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)

    parent_category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    
    parent_category = db.relationship(
        "Category",
        backref=db.backref("children", lazy=True),
        remote_side=[id]
    )


    def to_dict(self):
        return {
            "name": self.name
        }

    def __init__(self, name, parent_category_id):
        self.name = name
        self.parent_category_id = parent_category_id