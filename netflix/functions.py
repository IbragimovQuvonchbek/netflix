from hashlib import blake2b

from manageNetlix import ManageNetflix
from user import User, getData
from watchNetflix import showMovieList, WatchNetflix


def signup():
    name = input("name:")
    surname = input("surname:")
    username = input("username:")
    password = input("password:")
    currentUser = User(name, surname, username, password)
    currentUser.createNewUser()
    userId = currentUser.id
    return userId


def login():
    username = input("username:")
    password = input("password:")
    data = getData()
    userId = 0
    for user in data:
        if user['username'] == username and user['password'] == blake2b(password.encode('utf-8')).hexdigest():
            userId = user['id']
            break
    admin = isAdmin(username, password)
    return (userId, admin)


def addMovie():
    name = input("Movie name: ")
    description = input("Movie description: ")
    country = input("Movie country: ")
    year = input("Movie year: ")
    newMovie = ManageNetflix(movieName=name, movieYear=year, movieCountry=country, movieDescription=description)
    isAdded = newMovie.addMovie()
    print("successfully movie added" if isAdded else "this movie alreade exists")


def isAdmin(username, password):
    return username == "ibragimov10" and password == "abc123"


def likeMovie(userId, movieId):
    watch = WatchNetflix(userId)
    isAdded = watch.likeMovie(movieId)
    if isAdded:
        print("movie liked")
    else:
        print("movie disliked")


def watchMovie():
    showMovieList()
