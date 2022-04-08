from flask import render_template
from __init__ import app
from flask_login import login_required

from cruddy.app_crud import app_crud

app.register_blueprint(app_crud)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tbr/")
@login_required
def tbr():
    return render_template("tbr.html")


if __name__ == "__main__":
    app.run(debug=True)
