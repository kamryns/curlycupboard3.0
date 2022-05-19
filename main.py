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

@app.route("/songs/")
def songs():
    return render_template("songs.html")

@app.route("/scarlet/")
def scarlet():
    return render_template("scarletquiz.html")

@app.route("/romeo/")
def romeo():
    return render_template("romeo.html")

@app.route("/explorechoice/")
def echoice():
    return render_template("explorechoice.html")

@app.route("/exploredeeper/")
def edeeper():
    return render_template("exploredeeper.html")

@app.route("/startexploring/")
def starte():
    return render_template("startexploring.html")

@app.route('/dictionary/', methods=['GET','POST'])
def dictionary():
    try:
        keyword = request.form['keyword']
    except:
        keyword = "reading"
    url = "https://twinword-word-graph-dictionary.p.rapidapi.com/definition/"
    querystring = {"entry":keyword}
    headers = {
        'x-rapidapi-host': "twinword-word-graph-dictionary.p.rapidapi.com",
        'x-rapidapi-key': "3d43659d98msh26d5e705bc7d8b6p1d6431jsnba44357aaf20"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    if response.status_code<400:
        results = json.loads(response.content.decode("utf-8"))
        return render_template("dictionary.html", results=results, word=keyword)
    else:
        return render_template("dictionary.html", word=keyword)
    # print(response.text)

if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(
        host='127.0.0.1',
        debug=True,
        port=8080
    )