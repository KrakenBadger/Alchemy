from flask import Blueprint, render_template


root = Blueprint(
    "root",
    __name__
)


@root.route("/")
def landing():
    return render_template("landing.html")


@root.route("/home")
def index():
    return render_template("index.html")
