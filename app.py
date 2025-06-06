from flask import Flask, render_template, request
from checker import check_password_strength

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        password = request.form["password"]
        result = check_password_strength(password)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
