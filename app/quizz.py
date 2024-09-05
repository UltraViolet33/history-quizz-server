from flask import Blueprint, request, render_template, flash, redirect, url_for
from app.forms import QuizzForm
from app.models.Category import Category
from app.models.Quizz import Quizz


quizz = Blueprint("quizz", __name__)


@quizz.route("/all", methods=["GET"])
def all():
    quizzes = Quizz.query.all()
    print(quizzes)
    return render_template("quizz/all.html", quizzes=quizzes)


@quizz.route("/create", methods=["GET", "POST"])
def create():
    form = QuizzForm()
    form.category.choices = [(c.id, c.name) for c in Category.query.all()]
    form.category.choices.insert(0, ("", "Select Status"))

    if request.method == "POST":
        if form.validate_on_submit():
            quizz_title = form.title.data
            check_exits = Quizz.get_by_title(title=quizz_title)
            if not check_exits:
                # check if tit already exists
                quizz = Quizz(title=quizz_title)
                if form.category.data:
                    quizz.category_id = form.category.data
                quizz.save()
                flash(f"Catégorie {Quizz.title} ajouté", category="success")
                return redirect(url_for("quizz.all"))

            flash(f"Quizz {quizz_title} already exists")
    return render_template("quizz/create.html", form=form)


@quizz.route("/edit/<id>", methods=["GET", "POST"])
def edit_quizz(id):
    quizz = Quizz.query.filter_by(id=id).first()
    if not quizz:
        return "404", 404

    form = QuizzForm()
    form.category.choices = []
    if quizz.category:
        form.category.choices.insert(0, (quizz.category_id, quizz.category.name))
    else:
        form.category.choices.insert(0, ("", ""))

    for cat in Category.query.all():
        if cat.id != quizz.category_id:
            form.category.choices.append((cat.id, cat.name))

    if request.method == "GET":
        form.title.data = quizz.title

    if request.method == "POST":
        if form.validate_on_submit():
            quizz.title = form.title.data
            if form.category.data:
                quizz.category_id = form.category.data
            # check if tit already exists
            quizz.update()
            flash(f"Catégorie {quizz.title} modifiée", category="success")
            return redirect(url_for("quizz.all"))

    return render_template("quizz/edit.html", quizz=quizz, form=form)
