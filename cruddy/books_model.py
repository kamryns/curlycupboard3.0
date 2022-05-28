""" database dependencies to support Users db examples """
""" database dependencies to support Users db examples """
from sqlalchemy.exc import IntegrityError
from __init__ import db
from __init__ import app

# Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along
# Define variable to define type of database (sqlite), and name and location of myDB.db
dbURI = 'sqlite:///model/myDB.db'
# Setup properties for the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
app.config['SECRET_KEY'] = 'SECRET_KEY'
# Create SQLAlchemy engine to support SQLite dialect (sqlite:)


# Define the Users table within the model
# -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# -- a.) db.Model is like an inner layer of the onion in ORM
# -- b.) Users represents data we want to store, something that is built on db.Model
# -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL


class books(db.Model):
    # define the attend schema
    userID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=False, nullable=False)
    genre = db.Column(db.String(255), unique=False, nullable=False)
    dop = db.Column(db.String(255), unique=False, nullable=False)



    # constructor of a User object, initializes of instance variables within object
    def __init__(self, title, genre, author, dop):
        self.title = title
        self.genre = genre
        self.author = author
        self.dop = dop




# CRUD create/add a new record to the table
    # returns self or None on error
    def create1(self):
        try:
            # creates a person object from attend(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to attend table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read converts self to dictionary
    # returns dictionary
    def read1(self):
        return {
            "userID": self.userID,
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "dop": self.dop,
        }

    # CRUD update: updates attend name, res, food
    # returns self
    def update1(self, title, author, genre, dop):
        """only updates values with length"""
        if len(title) > 0:
            self.title = title
        if len(author) > 0:
            self.author = author
        if len(genre) > 0:
            self.genre = genre
        if len(genre) > 0:
            self.genre = genre

        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete1(self):
        db.session.delete(self)
        db.session.commit()
        return None


"""Database Creation and Testing section"""


def model_tester():
    print("--------------------------")
    print("Seed Data for Book Second Table: users")
    print("--------------------------")
    db.create_all()
    """Tester data for the second table"""
    u1 = books(title='Silent Patient', author='Alex Michaelides', genre='Thriller', dop='02/05/2019')
    u2 = books(title='Harry Potter', author='JK Rowling', genre='Fantasy', dop='06/26/1997')
    u3 = books(title='It Ends With Us', author='Colleen Hoover', genre='Romance', dop='08/02/2016')
    u4 = books(title='Crying in H Mart', author='Michelle Zauner', genre='Non-Fiction', dop='04/20/2021')

    table = [u1, u2, u3, u4]
    for row in table:
        try:
            db.session.add(row)
            db.session.commit()
        except IntegrityError:
            db.session.remove()



def model_printer():
    print("------------")
    print("Table: users with SQL query")
    print("------------")
    result = db.session.execute('select * from books')
    print(result.keys())
    for row in result:
        print(row)


if __name__ == "__main__":
    model_tester()  # builds model of books
    model_printer()