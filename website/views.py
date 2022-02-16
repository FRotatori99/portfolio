from flask import Blueprint, render_template
from datetime import date

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
def home():
    birthdate = date(day=28, month=3, year=1999)
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return render_template("home.html", age = age)

@views.route("/su-di-me/chi-sono")
def about_me():
    return render_template("su-di-me/about_me.html")

@views.route("/su-di-me/perchè-questo-sito")
def why_this_site():
    return render_template("su-di-me/why_this_site.html")

@views.route("/su-di-me/citazioni-preferite")
def quotes():
    return render_template("")

