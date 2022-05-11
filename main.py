from flask import Blueprint, render_template
from __init__ import app
from flask_login import login_required
from cruddy.app_crud import app_crud

app.register_blueprint(app_crud)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/notepad/")
def notepad():
    return render_template("notepad.html")

@app.route("/tbr/")
def tbr():
    return render_template("tbr.html")

@app.route("/draw/")
def draw():
    return render_template("draw.html")

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        debug=True,
        port=8080
    )