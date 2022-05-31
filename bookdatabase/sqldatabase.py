from __init__ import db
from bookdatabase.modeldatabase import Books
import random


# this is method called by frontend, it has been randomized between Alchemy and Native SQL for fun
def books_all():
    if random.randint(0, 1) == 0:
        table = books_all_alc()
    else:
        table = books_all_sql()
    return table


# SQLAlchemy extract all users from database
def books_all_alc():
    table = Books.query.all()
    json_ready = [peep.read() for peep in table]
    return json_ready


# Native SQL extract all users from database
def books_all_sql():
    table = db.session.execute('select * from books')
    json_ready = sqlquery_2_list(table)
    return json_ready


# SQLAlchemy extract users from database matching term
def books_ilike(term):
    """filter Users table by term into JSON list (ordered by User.name)"""
    term = "%{}%".format(term)  # "ilike" is case insensitive and requires wrapped  %term%
    table = Books.query.order_by(Books.name).filter((Books.name.ilike(term)) | (Books.book.ilike(term)))
    return [peep.read() for peep in table]


# SQLAlchemy extract single user from database matching ID
def book_by_id(bookid):
    """finds User in table matching userid """
    print("in book by id method"+bookid)
    return Books.query.filter_by(bookID=bookid).first()


# SQLAlchemy extract single user from database matching book
def book_by_book(book):
    """finds User in table matching book """
    return Books.query.filter_by(book=book).first()


# ALGORITHM to convert the results of an SQL Query to a JSON ready format in Python
def sqlquery_2_list(rows):
    out_list = []
    keys = rows.keys()  # "Keys" are the columns of the sql query
    for values in rows:  # "Values" are rows within the SQL database
        row_dictionary = {}
        for i in range(len(keys)):  # This loop lines up K, V pairs, same as JSON style
            row_dictionary[keys[i]] = values[i]
        row_dictionary["query"] = "by_sql"  # This is for fun a little watermark
        out_list.append(row_dictionary)  # Finally we have a out_list row
    return out_list


# Test queries
if __name__ == "__main__":
    for i in range(1):
        print(books_all())
