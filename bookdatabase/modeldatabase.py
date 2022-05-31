""" database dependencies to support Users db examples """
from sqlalchemy.exc import IntegrityError
from __init__ import db

# Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along


# Define the Users table within the model
# -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# -- a.) db.Model is like an inner layer of the onion in ORM
# -- b.) Users represents data we want to store, something that is built on db.Model
# -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL
class Books(db.Model):
    # define the Users schema
    bookID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    book = db.Column(db.String(255), unique=False, nullable=False)
    review = db.Column(db.String(255), unique=False, nullable=False)

    # constructor of a User object, initializes of instance variables within object
    def __init__(self, name, book, review):
        self.name = name
        self.book = book
        self.review = review

    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        try:
            # creates a person object from Users(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read converts self to dictionary
    # returns dictionary
    def read(self):
        return {
            "bookID": self.bookID,
            "name": self.name,
            "book": self.book,
            "review": self.review,
            "query": "by_alc"  # This is for fun, a little watermark
        }

    # CRUD update: updates users name, password, phone
    # returns self
    def update(self, review):
        """only updates values with length"""
        if len(review) > 0:
            self.review = review
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None


"""Database Creation and Testing section"""


def model_tester():
    print("--------------------------")
    print("Seed Data for Table: books")
    print("--------------------------")
    db.create_all()
    """Tester data for table"""
    u1 = Books(name='Thomas Edison', book='San Diego', review='loved the weather')
    u2 = Books(name='Nicholas Tesla', book='San Francisco', review='terrible traffic')
    u3 = Books(name='Alexander Graham Bell', book='Tokyo', review='worst place i have ever visited')
    u4 = Books(name='Eli Whitney', book='Mumbai', review='fantastic food')
    u5 = Books(name='John Mortensen', book='Berlin', review='great historical sites')
    u6 = Books(name='John Mortensen', book='New York City', review='worst traffic i have experienced in my life')
    # U7 intended to fail as duplicate key
    u7 = Books(name='John Mortensen', book='Orlando', review='disneyland is fun')
    table = [u1, u2, u3, u4, u5, u6, u7]
    for row in table:
        try:
            db.session.add(row)
            db.session.commit()
        except IntegrityError:
            db.session.remove()
            print(f"Records exist, duplicate book, or error: {row.book}")


def model_printer():
    print("------------")
    print("Table: books with SQL query")
    print("------------")
    result = db.session.execute('select * from books')
    print(result.keys())
    for row in result:
        print(row)


if __name__ == "__main__":
    model_tester()  # builds model of Users
    model_printer()
