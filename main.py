from __init__ import app
from cruddy.app_crud import app_crud
from flask import render_template, request
import requests
import json
from notey.app_notes import app_notes
from contenty.app_content import app_content
import pickle
from flask_login import login_required, current_user


app.register_blueprint(app_content)
app.register_blueprint(app_crud)
app.register_blueprint(app_notes)

from bookdatabase.app_database import app_database
app.register_blueprint(app_database)

thisList = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tools/")

def tools():
    return render_template("tools.html")

@app.route("/plant/")
@login_required
def plant():
    return render_template("plant.html")

@app.route("/notepad/")
@login_required
def notepad():
    return render_template("notepad.html")

@app.route("/tbr/")
@login_required
def tbr():
    return render_template("tbr.html")

@app.route("/draw/")
@login_required
def draw():
    return render_template("draw.html")

@app.route("/songs/")
@login_required
def songs():
    return render_template("songs.html")

@app.route("/calender/")
@login_required
def calender():
    return render_template("calender.html")

@app.route("/scarlet/")
def scarlet():
    return render_template("scarletquiz.html")


@app.route("/summer/")
def summer():
    return render_template("summer.html")

@app.route("/romeo/")
def romeo():
    return render_template("romeo.html")

@app.route("/explorechoice/")
@login_required
def echoice():
    return render_template("explorechoice.html")

@app.route("/exploredeeper/")
@login_required
def edeeper():
    return render_template("exploredeeper.html")

@app.route("/startexploring/")
@login_required
def starte():
    return render_template("startexploring.html")

@app.route("/crossword/")
@login_required
def crossword():
    return render_template("crossword.html")

@app.route("/timer/")
@login_required
def timer():
    return render_template("timer.html")

@app.route('/dictionary/', methods=['GET','POST'])
@login_required
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

@app.route('/flashcards/')
@login_required
def flashcards():
    return render_template("flashcards.html")

@app.route('/beginnerforum/')
@login_required
def beginnerforum():
    return render_template("startexploring.html")


@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.form:
        thought = request.form.get("thought")
        thisList.append(thought)
        if len(thought) != 0:
            return render_template("startexploring.html", nickname=thisList)
    return render_template("startexploring.html")


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if len(thisList) > 0:
        thisList.pop(len(thisList) - 1)
    return render_template("startexploring.html", nickname=thisList)

@app.route('/bookwheel/')
def bookwheel():
    return render_template("bookwheel.html")

@app.route('/reviews/', methods=['GET'])
def reviews():
    #kdf = open('KammyDebug.txt', 'wt+')
    #fileInfoStorage = open('/Users/kamrynsinsuan/IdeaProjects/curlycupboard3.0/reviews.bin', 'rb')
    try:
        #dataDict = pickle.load(fileInfoStorage)
        tmpComments = dataDict['tmpTotalComment']
        #kdf.writelines('Retreiving Comments: %s\n' % dataDict['tmpTotalComment'])
    except:
        tmpComments = ""

    attrib_names = [
        {'labelName': "Book:", "textAreaName": "movie", "placeholderName": "Title", "rows": "1", "cols": "32"},
        {'labelName': "Rating:", "textAreaName": "rating", "placeholderName": "1-5", "rows": "1", "cols": "32"},
        {'labelName': "Comment:", "textAreaName": "comment", "placeholderName": "Review!", "rows": "10", "cols": "32"},
    ]

    #fileInfoStorage.close()
    #kdf.close()
    return render_template("reviews.html", attrib_names=attrib_names, persistentComments=tmpComments)

@app.route('/reviews/', methods=['POST'])
def storeComments():
    #kdf = open('KammyDebug.txt', 'wt+')
    #fileInfoStorage = open('/Users/kamrynsinsuan/IdeaProjects/curlycupboard3.0/reviews.bin', 'wb+')
    blob = request.data
    dataDict = json.loads(bytes.decode(blob))
    #pickle.dump(dataDict, fileInfoStorage)
    #kdf.writelines('Storing Comments: %s\n' % dataDict)
    #kdf.close()
    #fileInfoStorage.close()
    return render_template("reviews.html")

if __name__ == "__main__" :
    # runs the application on the repl development server
    app.run(debug=True, port="5224")