from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        password = request.form["password"]
        # your checker logic...
        return render_template("index.html", password=password, strength="Strong", suggestions=[])
    return render_template("index.html")
