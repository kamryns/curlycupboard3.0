"""control dependencies to support CRUD app routes and APIs"""
from flask import Blueprint, render_template, request, url_for, redirect, jsonify, make_response

from bookdatabase.sqldatabase import *

# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects
app_database = Blueprint('database', __name__,
                     url_prefix='/database',
                     template_folder='templates/database/',
                     static_folder='static',
                     static_url_path='static')

""" Application control for CRUD is main focus of this File, key features:
    1.) User table queries
    2.) app routes for CRUD (Blueprint)
"""


# Default URL
@app_database.route('/')
def database():
    """obtains all Users from table and loads Admin Form"""
    return render_template("database.html", table=books_all())


# CRUD create/add
@app_database.route('/create/', methods=["POST"])
def create():
    """gets data from form and add it to Users table"""
    if request.form:
        po = Books(
            request.form.get("name"),
            request.form.get("book"),
            request.form.get("review"),
        )
        po.create()
    return redirect(url_for('database.database'))


# CRUD read
@app_database.route('/read/', methods=["POST"])
def read():
    """gets userid from form and obtains corresponding data from Users table"""
    table = []
    if request.form:
        bookid = request.form.get("bookid")
        po = book_by_id(bookid)
        if po is not None:
            table = [po.read()]  # placed in list for easier/consistent use within HTML
    return render_template("database.html", table=table)


# CRUD update
@app_database.route('/update/', methods=["POST"])
def update():
    """gets userid and name from form and filters and then data in  Users table"""
    if request.form:
        bookid = request.form.get("bookid")
        review = request.form.get("review")
        po = book_by_id(bookid)
        print("here")
        print(po)
        if po is not None:
            po.update(review)
    return redirect(url_for('database.database'))


# CRUD delete
@app_database.route('/delete/', methods=["POST"])
def delete():
    """gets userid from form delete corresponding record from Users table"""
    if request.form:
        bookid = request.form.get("bookid")
        po = book_by_id(bookid)
        if po is not None:
            po.delete()
    return redirect(url_for('database.database'))


# Search Form
@app_database.route('/search/')
def search():
    """loads form to search Users data"""
    return render_template("searchdatabase.html")


# Search request and response
@app_database.route('/search/term/', methods=["POST"])
def search_term():
    """ obtain term/search request """
    req = request.get_json()
    term = req['term']
    response = make_response(jsonify(books_ilike(term)), 200)
    return response
