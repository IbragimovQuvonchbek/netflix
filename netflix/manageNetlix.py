import json

from watchNetflix import getData


class ManageNetflix:
    id = 0

    def __init__(self, movieName, movieYear,movieDuration, movieCountry, movieDescription):
        self.movieName = movieName
        self.movieYear = movieYear
        self.movieCountry = movieCountry
        self.movieDuration = movieDuration
        self.movieDescription = movieDescription

    def addMovie(self):
        if not self.isAvailable():
            data = getData()
            self.id = 1 if not data else data[-1]['id'] + 1
            newMovie = {
                "id": self.id,
                "name": self.movieName,
                "country": self.movieCountry,
                "duration": self.movieDuration,
                "year": self.movieYear,
                "description": self.movieDescription,
                "likes": 0,
            }
            data.append(newMovie)
            with open('netflix.json', 'w') as f:
                json.dump(data, f, indent=4)
            return True
        return False

    def isAvailable(self):
        data = getData()
        for user in data:
            if user['name'] == self.movieName:
                return True
        return False
