from statistics import median, mean
from flask import Flask, flash, render_template, request, url_for, redirect
from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    login_required,
    current_user,
)

from models import Customer, dbase
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config.from_object('config')

login_manager = LoginManager(app)
login_manager.login_view = "log_page"

with app.app_context():
    dbase.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return Customer.query.get(int(user_id))

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/reg_page", methods=["GET"])
def register_page():
    return render_template("reg_page.html")

@app.route("/reg_page", methods=["POST"])
def registr_form():
    username = request.form["email"]
    password = request.form["password"]
    if Customer.query.filter_by(username=username).first():
        flash(f"The username already exist.")
        return redirect(url_for("register_page"))
    
    user = Customer(username=username, password=password)
    dbase.session.add(user)
    login_user(user)
    flash(f"Welcome {username}!")
    return redirect(url_for("index"))

@app.route("/log_page", methods=["GET"])
def login_page():
    return render_template("log_page.html")

@app.route("/log_page", methods=["POST"])
def login_form():
    username = request.form["email"]
    password = request.form["password"]
    user =  Customer.query.filter_by(username=username).first()
    if not user:
        flash(f"Incorrect username. Try again!")
        return redirect(url_for("login_page"))
    if password != user.password:
        flash(f"Invalid password. Try again!")
        return redirect(url_for("login_page"))

    login_user(user)
    flash(f"Welcome back, {username}!")
    return redirect(url_for("index"))

@app.route("/logout_page", methods=["GET"])
@login_required
def logout():
    return render_template("logout_page.html")

@app.route("/logout_page", methods=["POST"])
@login_required
def logout_form():
    logout_user()
    flash("Log out successfull.")
    return redirect(url_for("index"))

@app.route("/tools.html")
def tools():
    return render_template("tools.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/delivery")
def delivery():
    return render_template("delivery.html")