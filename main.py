from __init__ import app
from cruddy.app_crud import app_crud
from flask import render_template, request
import requests
import json
from notey.app_notes import app_notes
from contenty.app_content import app_content
import pickle



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
def plant():
    return render_template("plant.html")

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

@app.route("/calender/")
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
def echoice():
    return render_template("explorechoice.html")

@app.route("/exploredeeper/")
def edeeper():
    return render_template("exploredeeper.html")

@app.route("/startexploring/")
def starte():
    return render_template("startexploring.html")

@app.route("/crossword/")
def crossword():
    return render_template("crossword.html")

@app.route("/timer/")
def timer():
    return render_template("timer.html")

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

@app.route('/flashcards/')
def flashcards():
    return render_template("flashcards.html")

@app.route('/beginnerforum/')
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

@app.route('/rewording/', methods=['GET', 'POST'])
def rewording():
    if request.form:
        url = "https://rimedia-paraphraser.p.rapidapi.com/api_paraphrase.php"
        user_text = request.form.get("user_text")
        if len(user_text) != 0:
            querystring = {"text": user_text, "lang":"en"}
            headers = {
                'content-type': "application/x-www-form-urlencoded",
                'x-rapidapi-host': "rimedia-paraphraser.p.rapidapi.com",
                'x-rapidapi-key': "e2d0d1a7efmsh5668be741c711ffp1a3e44jsnfc9e0a91c2b2"
            }
            response = requests.request("POST", url, data=querystring, headers=headers)
            return render_template("rewording.html", results=response.json())
    else:
        return render_template("rewording.html", results="")

@app.route('/reviews/', methods=['GET'])
def reviews():
    #kdf = open('KammyDebug.txt', 'wt+')
    #fileInfoStorage = open('/reviews.bin', 'rb')
    try:
        #dataDict = pickle.load(fileInfoStorage)
        tmpComments = dataDict['tmpTotalComment']
        #kdf.writelines('Retreiving Comments: %s\n' % dataDict['tmpTotalComment'])
    except:
        tmpComments = ""

    attrib_names = [
        {'labelName': "Books:", "textAreaName": "movie", "placeholderName": "Title", "rows": "1", "cols": "32"},
        {'labelName': "Rating:", "textAreaName": "rating", "placeholderName": "1-5", "rows": "1", "cols": "32"},
        {'labelName': "Comment:", "textAreaName": "comment", "placeholderName": "Review!", "rows": "10", "cols": "32"},
    ]

    #fileInfoStorage.close()
    #kdf.close()
    return render_template("reviews.html", attrib_names=attrib_names, persistentComments=tmpComments)

@app.route('/reviews/', methods=['POST'])
def storeComments():
    # kdf = open('KammyDebug.txt', 'wt+')
    #fileInfoStorage = open('templates/reviews.bin', 'wb+')
    blob = request.data
    dataDict = json.loads(bytes.decode(blob))
    pickle.dump(dataDict, fileInfoStorage)
    #kdf.writelines('Storing Comments: %s\n' % dataDict)
    #kdf.close()
    #fileInfoStorage.close()
    return render_template("reviews.html")

if __name__ == "__main__" :
    # runs the application on the repl development server
    app.run(debug=True, port="5224")