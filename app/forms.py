from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    BooleanField,
    TextAreaField,
    SelectField,
    IntegerField,
    SelectMultipleField,
    TextAreaField,
)
from wtforms.validators import DataRequired


class CategoryForm(FlaskForm):
    name = StringField("Nom", validators=[DataRequired()])


class QuizzForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    category = SelectField("Category")
