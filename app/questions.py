from flask import Blueprint, request, render_template, flash, redirect, url_for
from werkzeug.utils import secure_filename
from app.models.Answer import Answer
from app.models.Question import Question
import json
import os


questions = Blueprint("questions", __name__)

app_folder = os.path.dirname(os.path.abspath(__file__))
questions_folder = os.path.join(app_folder, "questions_files")


@questions.route("/import-questions", methods=["GET", "POST"])
def import_questions():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['file']
        
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(questions_folder, filename))
            import_questions_from_file(os.path.join(questions_folder, filename))
            # Further processing of the file can be done here
            flash('File successfully uploaded')
            return redirect(url_for('questions.import_questions'))
    return render_template("questions/import.html")


@questions.route("/generate-json-file", methods=["GET"])
def generate_json():
    json_questions = []
    questions = Question.query.all()

    for question in questions:
        question_dict = {
            "id": question.id,
            "question": question.text,
            "answer1": question.right_answer.text,
        }
        i = 2
        for answer in question.answers:
            question_dict[f"answer{i}"] = answer.text
            i += 1
        json_questions.append(question_dict)
        filename = os.path.join(questions_folder, 'questions.json')

        with open(filename, 'w') as f:
            json.dump(json_questions, f)


    return json_questions


def import_questions_from_file(filename):
    with open(filename) as file:
        for line in file:
            print(line.rstrip())
            if line == '\n':
                continue
            typet, text = line.split(':')
            if typet == 'question':
                question_text = text
            if typet == 'answer1':
                right_answer = Answer(text)
                right_answer.save()
            if typet == 'answer2':
                answer2 = Answer(text)
                answer2.save()
            if typet == 'answer3':
                answer3 = Answer(text)
                answer2.save()

            if typet == 'answer4':
                answer4 = Answer(text)
                answer4.save()
                question = Question(question_text, right_answer.id)
                question.save()
                question.answers.append(answer2)
                question.answers.append(answer3)
                question.answers.append(answer4)

                question.update()