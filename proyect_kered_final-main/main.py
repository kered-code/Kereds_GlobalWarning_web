from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route("/next")
def next():
    return render_template("next.html")

@app.route("/aply")
def aply():
    return render_template("aply.html")




if __name__ == '__main__':
    app.run(debug=True)
