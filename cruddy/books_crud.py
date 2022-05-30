#still need to add in search html and database for books


"""control dependencies to support CRUD app routes and APIs"""
from flask import Blueprint, render_template, request, url_for, redirect, jsonify, make_response

from cruddy.sql import *

# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects
app_books = Blueprint('boks', __name__,
                       url_prefix='/books',
                       template_folder='templates/books/',
                       static_folder='static',
                       static_url_path='assets')

""" Application control for CRUD is main focus of this File, key features:
    1.) User table queries
    2.) app routes for CRUD (Blueprint)
"""


# Default URL
@books_crud.route('/')
def crud():
    """obtains all Users from table and loads Admin Form"""
    return render_template("crud.html", table=users_all())


# CRUD create/add
@books_crud.route('/create/', methods=["POST"])
def create():
    """gets data from form and add it to Users table"""
    if request.form:
        po = books(
            request.form.get("title"),
            request.form.get("author"),
            request.form.get("genre"),
            request.form.get("dop")
        )
        po.create()
    return redirect(url_for('crud.crud'))


# CRUD read
@books_crud.route('/read/', methods=["POST"])
def read():
    """gets userid from form and obtains corresponding data from Users table"""
    table = []
    if request.form:
        userid = request.form.get("userid")
        po = user_by_id(userid)
        if po is not None:
            table = [po.read()]  # placed in list for easier/consistent use within HTML
    return render_template("crud.html", table=table)


# CRUD update
@books_crud.route('/update/', methods=["POST"])
def update():
    """gets userid and name from form and filters and then data in  Users table"""
    if request.form:
        userid = request.form.get("userid")
        name = request.form.get("name")
        po = user_by_id(userid)
        if po is not None:
            po.update(name)
    return redirect(url_for('crud.crud'))


# CRUD delete
@books_crud.route('/delete/', methods=["POST"])
def delete():
    """gets userid from form delete corresponding record from Users table"""
    if request.form:
        userid = request.form.get("userid")
        po = user_by_id(userid)
        if po is not None:
            po.delete()
    return redirect(url_for('crud.crud'))


# Search Form
@books_crud.route('/search/')
def search():
    """loads form to search Users data"""
    return render_template("search.html")


# Search request and response
@books_crud.route('/search/term/', methods=["POST"])
def search_term():
    """ obtain term/search request """
    req = request.get_json()
    term = req['term']
    response = make_response(jsonify(users_ilike(term)), 200)
    print(response)
    return response