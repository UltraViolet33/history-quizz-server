from flask import Blueprint, render_template, redirect
from flask_login import logout_user, login_required, current_user


auth = Blueprint("auth", __name__)


@auth.route("/", methods=["GET", "POST"])
def login():

    return render_template("login.html", user=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/login")
