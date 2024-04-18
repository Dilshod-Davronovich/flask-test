from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def start():
    return "Server ishladi"

@app.route("/about")
def about():
    return render_template("index.html")


