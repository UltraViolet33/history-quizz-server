from flask import Blueprint, request, render_template, flash, redirect, url_for
from app.forms import CategoryForm
from app.models.Category import Category


categories = Blueprint("categories", __name__)


@categories.route("/all", methods=["GET"])
def all():
    categories = Category.query.all()
    return render_template("categories/all.html", categories=categories)


@categories.route("/create", methods=["GET", "POST"])
def create():
    form = CategoryForm()

    if request.method == "POST":
        if form.validate_on_submit():
            category_name = form.name.data
            check_exits = Category.get_by_name(name=category_name)
            if not check_exits:
                # check if name already exists
                category = Category(name=category_name)
                category.save()
                flash(f"Catégorie {category.name} ajouté", category="success")
                return redirect(url_for("categories.all"))

            flash(f"Category {category_name} already exists")
    return render_template("categories/create.html", form=form)


@categories.route("/edit/<id>", methods=["GET", "POST"])
def edit_category(id):
    category = Category.query.filter_by(id=id).first()
    if not category:
        return "404", 404

    form = CategoryForm()
    if request.method == "GET":
        form.name.data = category.name

    if request.method == "POST":
        if form.validate_on_submit():
            category.name = form.name.data
            # check if name already exists
            category.update()
            flash(f"Catégorie {category.name} modifiée", category="success")
            return redirect(url_for("categories.all"))

    return render_template("categories/edit.html", category=category, form=form)
