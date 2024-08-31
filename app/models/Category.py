from .Model import Model
from .. import db




class Category(db.Model, Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)


    def to_dict(self):
        return {
            "name": self.name
        }

    def __init__(self, name):
        self.name = name