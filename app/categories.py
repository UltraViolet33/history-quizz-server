from flask import Blueprint, request
from . import db
from .models.Category import Category
from sqlalchemy.sql.expression import func


categories = Blueprint("categories", __name__)


@categories.route("/all", methods=["GET"])
def get_all_categories():

    return {"data": []}
