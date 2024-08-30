from flask import Blueprint, render_template


questions = Blueprint("questions", __name__)


# @questions.route("/", methods=["GET", "POST"])
# def all_questions():
#     return render_template("questions/all.html")
