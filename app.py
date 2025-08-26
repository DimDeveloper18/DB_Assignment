from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/tools.html")
def tools():
    return render_template("tools.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/delivery")
def delivery():
    return render_template("delivery.html")