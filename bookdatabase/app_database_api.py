"""control dependencies to support CRUD routes and APIs"""
from flask import Blueprint, render_template
from flask_restful import Api, Resource
import requests

from bookdatabase.sqldatabase import *

# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects

app_database_api = Blueprint('database_api', __name__,
                         url_prefix='/database_api',
                         template_folder='templates/database/',
                         static_folder='static',
                         static_url_path='static')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(app_database_api)


# Method #2 for CRUD
@app_database_api.route('/')
def database_api():
    """obtains all Users from table and loads Admin Form"""
    return render_template("database_async.html", table=books_all())


""" API routes section """


class BooksAPI:
    # class for create/post
    class _Create(Resource):
        def post(self, name, book, review):
            po = Books(name, book, review)
            person = po.create()
            if person:
                return person.read()
            return {'message': f'Processed {name}, either a format error or {book} is duplicate'}, 210

    # class for read/get
    class _Read(Resource):
        def get(self):
            return books_all()

    # class for delete
    class _ReadID(Resource):
        def get(self, bookid):
            po = book_by_id(bookid)
            if po is None:
                return {'message': f"{bookid} is not found"}, 210
            data = po.read()
            return data

    # class for read/get
    class _ReadILike(Resource):
        def get(self, term):
            return books_ilike(term)

    # class for update/put
    class _Update(Resource):
        def put(self, book, name):
            po = book_by_book(book)
            if po is None:
                return {'message': f"{book} is not found"}, 210
            po.update(name)
            return po.read()

        # class for update/put

    class _UpdateName(Resource):
        def put(self, bookid, name):
            po = book_by_id(bookid)
            if po is not None:
                po.update(name)
            return po.read()

    class _UpdateAll(Resource):
        def put(self, book, name, review):
            po = book_by_book(book)
            if po is None:
                return {'message': f"{book} is not found"}, 210
            po.update(name, review)
            return po.read()

    # class for delete
    class _Delete(Resource):
        def delete(self, bookid):
            po = book_by_id(bookid)
            if po is None:
                return {'message': f"{bookid} is not found"}, 210
            data = po.read()
            po.delete()
            return data

    # building RESTapi resource
    # building RESTapi resource
    api.add_resource(_Create, '/create/<string:name>/<string:book>/<string:review>/')
    api.add_resource(_Read, '/read/')
    api.add_resource(_ReadID, '/read/<int:bookid>')
    api.add_resource(_ReadILike, '/read/ilike/<string:term>')
    api.add_resource(_Update, '/update/<string:book>/<string:name>')
    api.add_resource(_UpdateName, '/update/<int:bookid>/<string:name>')
    api.add_resource(_UpdateAll, '/update/<string:book>/<string:name>/<string:review>/')
    api.add_resource(_Delete, '/delete/<int:bookid>')


""" API testing section """


def api_tester():
    # local host URL for model
    url = 'http://localhost:5222/database_api'

    # test conditions
    API = 0
    METHOD = 1
    tests = [
        ['/create/Wilma Flintstone/wilma@bedrock.org/123wifli/0001112222', "post"],
        ['/create/Fred Flintstone/fred@bedrock.org/123wifli/0001112222', "post"],
        ['/read/', "get"],
        ['/read/1', "get"],
        ['/read/ilike/John', "get"],
        ['/read/ilike/com', "get"],
        ['/update/wilma@bedrock.org/Wilma S Flintstone/123wsfli/0001112229', "put"],
        ['/update/wilma@bedrock.org/Wilma Slaghoople Flintstone', "put"],
        ['/delete/4', "delete"],
        ['/read/4', "get"],
        ['/delete/5', "delete"],
        ['/read/5', "get"],
        ['/update/1/Thomas Alva Edison', "put"]
    ]

    # loop through each test condition and provide feedback
    for test in tests:
        print()
        print(f"({test[METHOD]}, {url + test[API]})")
        if test[METHOD] == 'get':
            response = requests.get(url + test[API])
        elif test[METHOD] == 'post':
            response = requests.post(url + test[API])
        elif test[METHOD] == 'put':
            response = requests.put(url + test[API])
        elif test[METHOD] == 'delete':
            response = requests.delete(url + test[API])
        else:
            print("unknown RESTapi method")
            continue

        print(response)
        try:
            print(response.json())
        except:
            print("unknown error")


def api_printer():
    print()
    print("Books table")
    for book in books_all():
        print(book)


"""validating api's requires server to be running"""
if __name__ == "__main__":
    api_tester()
    api_printer()
