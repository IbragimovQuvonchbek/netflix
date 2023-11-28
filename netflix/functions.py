from hashlib import blake2b

from cart import Cart
from manageNetlix import ManageNetflix
from user import User, getData
from watchNetflix import getData as movies
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
    admin = False
    for user in data:
        if user['username'] == username and user['password'] == blake2b(password.encode('utf-8')).hexdigest():
            userId = user['id']
            admin = user['isAdmin']
            break
    return userId, admin


def addMovie():
    name = input("Movie name: ")
    description = input("Movie description: ")
    country = input("Movie country: ")
    year = input("Movie year: ")
    newMovie = ManageNetflix(movieName=name, movieYear=year, movieCountry=country, movieDescription=description)
    isAdded = newMovie.addMovie()
    print("successfully movie added" if isAdded else "this movie alreade exists")


def likeMovie(userId, movieId):
    watch = WatchNetflix(userId)
    isAdded = watch.likeMovie(movieId)
    if isAdded:
        print("movie liked")
    else:
        print("movie disliked")


def saveMovie(userId, movieId):
    save = Cart(userId)
    isSaved = save.saveMovie(movieId)
    if isSaved:
        print("movie Saved")
    else:
        print("movie Unsaved")


def filterByDuration():
    data = movies()
    for movie in data:
        date = movie["duration"]
        dur = dict()
        if 'h' in date:
            x = date.split('h')
            dur['h'] = int(x[0])
        if "min" in date:
            dur['min'] = int(date[date.index('min') - 2:date.index('min')])
        if 'h' in list(dur.keys()):
            if dur['h'] >= 2 and 'min' in list(dur.keys()):
                print("-" * len(movie['description']))
                print(f"id: {movie['id']}")
                print(f"Movie Name: {movie['name']}")
                print(f"Movie description: {movie['description']}")
                print(f"Movie Contry: {movie['country']}")
                print(f"Movie Duration: {movie['duration']}")
                print(f"Movie Year: {movie['year']}")
                print(f"Likes: {movie['likes']}")
                print("-" * len(movie['description']))


def showSavedMovies(userId):
    save = Cart(userId)
    save.showSavedMovies()


def watchMovie():
    showMovieList()
