from statistics import median, mean
import os
from flask import Flask, flash, render_template, request, url_for, redirect
from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    login_required,
    current_user,
)

from models import Customer, CustomerComment, dbase
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config.from_object('config')

login_manager = LoginManager(app)
login_manager.login_view = "login_page"

with app.app_context():
    dbase.init_app(app)
    dbase.create_all()

@login_manager.user_loader
def load_user(user):
    print(user)
    return Customer.query.get(int(user))

# def recomment(comment_body):
#     return comment_body.writer == current_user

@app.route("/")
@app.route("/index")
def index_page():
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
    dbase.session.commit()
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
    print(user)
    if not user:
        flash(f"Incorrect username. Try again!")
        return redirect(url_for("login_page"))
    if password != user.password:
        flash(f"Invalid password. Try again!")
        return redirect(url_for("login_page"))

    login_user(user)
    flash(f"Welcome back, {username}!")
    return redirect(url_for("comments_page"))

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

@app.route("/tools", methods=["GET"])
def tools_page():
    return render_template("tools.html", comments=CustomerComment.query.all())



@app.route("/contact")
def contact_page():
    return render_template("contact.html")

@app.route("/comments", methods=["GET"])
@login_required
def comments_page():
    return render_template("comments.html")

@app.route("/comments", methods=["POST"])
@login_required
def comment_create():
    if request.method == "POST":
        comment_body = CustomerComment(
        msgname=request.form["msgname"],
        comment=request.form["comment_text"],
        writer=current_user
    )
        print(comment_body)
        dbase.session.add(comment_body)
        dbase.session.commit()
        return redirect(url_for("tools"))
    flash("Commit.")
    return render_template(url_for("coments_page"))

# @app.route("/update_comment/<int:comment_id>", method=["GET"])
# @login_required
# def upcom_page(comment_id):
#     comment_body = CustomerComment.query.get_or_404(comment_id)
#     if not recomment(comment_body):
#         flash(f"Comment update allowed to owner only")
#         return redirect(url_for("comment_body", comment_id=comment.id))
    
#     return render_template("updat_comment.html" comment_body=comment_body)

# @app.route("/update_comment/<int:comment_id>", method=["POST"])
# @login_required
# def recomment(comment_id):
#     comment_body = CustomerComment.query.get_or_404(comment_id)
#     if not recomment(comment_body):
#         flash(f"Comment update allowed to owner only")
#         return redirect(url_for("comment_body", comment_id=comment.id))
#     comment_body.msgname = request.form["msgname"]
#     comment_body.comment = request.form["comment"]
#     dbase.session.commit()
#     return redirect(url_for("comment_body", comment_id=comment.id))

@app.route("/delivery")
def delivery_page():
    return render_template("delivery.html")

if __name__ == "__main__":
    if not os.path.exists("database.db"):
        dbase.create_all()
    app.run(debug=True)