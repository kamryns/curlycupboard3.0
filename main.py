from flask import Blueprint, render_template
from __init__ import app
from flask_login import login_required
from cruddy.app_crud import app_crud
from flask import render_template, request
import requests
import json

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

@app.route("/scarlet/")
def scarlet():
    return render_template("scarletquiz.html")

@app.route("/romeo/")
def romeo():
    return render_template("romeo.html")

@app.route("/explorechoice/")
def echoice():
    return render_template("explorechoice.html")



if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(
        host='127.0.0.1',
        debug=True,
        port=8080
    )