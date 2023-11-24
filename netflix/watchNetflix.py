import json


def getData():
    try:
        with open('netflix.json') as f:
            data = json.load(f)
        return data
    except (FileNotFoundError, json.JSONDecodeError):
        with open('netflix.json', 'w') as f:
            json.dump([], f)
        return []


def showMovieList():
    for movie in getData():
        print(f"id: {movie['id']}")
        print(f"Movie Name: {movie['name']}")
        print(f"Movie description: {movie['description']}")
        print(f"Movie Contry: {movie['country']}")
        print(f"Movie Year: {movie['year']}")
        print(f"Likes: {movie['likes']}")
        print("-" * len(movie['description']))


class WatchNetflix:
    def getDataWatch(self):
        try:
            with open('watchNetflix.json') as f:
                data = json.load(f)
            return data
        except (FileNotFoundError, json.JSONDecodeError):
            with open('watchNetflix.json', 'w') as f:
                json.dump([], f)
            return []

    def __init__(self, userId):
        self.userId = userId
        data = self.getDataWatch()
        isFound = False
        for detail in data:
            if detail['userId'] == userId:
                self.likedMovies = detail['likedMovies']
                isFound = True
                break
        if not isFound:
            newUser = {
                "id": 1 if not data else data[-1]["id"] + 1,
                "userId": userId,
                "likedMovies": []
            }
            data.append(newUser)
            with open('watchNetflix.json', 'w') as f:
                json.dump(data, f, indent=4)

            self.likedMovies = []

    def likeMovie(self, movieId):
        data = getData()
        for movie in data:
            if movie['id'] == movieId:
                if movie['id'] in self.likedMovies:
                    movie['likes'] -= 1
                    self.likedMovies.remove(movie['id'])
                    with open('netflix.json', 'w') as f:
                        json.dump(data, f, indent=4)
                    data = self.getDataWatch()
                    for details in data:
                        if details['userId'] == self.userId:
                            details['likedMovies'] = self.likedMovies
                            with open('watchNetflix.json', 'w') as f:
                                json.dump(data, f, indent=4)
                            break
                    return False
                else:
                    self.likedMovies.append(movie['id'])
                    movie['likes'] += 1
                    with open('netflix.json', 'w') as f:
                        json.dump(data, f, indent=4)
                    data = self.getDataWatch()
                    for details in data:
                        if details['userId'] == self.userId:
                            details['likedMovies'] = self.likedMovies
                            with open('watchNetflix.json', 'w') as f:
                                json.dump(data, f, indent=4)
                            break
                    return True
        return False
