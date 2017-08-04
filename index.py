from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods = ["POST"])
def result():
    name_val = request.form["name_key"]
    location_val = request.form["location_key"]
    language_val = request.form["language_key"]
    comment_val = request.form["comment_key"]

    return render_template("result.html", name = name_val, location = location_val, language = language_val, comment = comment_val)

app.run(debug = True)