import json

from watchNetflix import getData


def getDataCart():
    try:
        with open('cart.json') as f:
            data = json.load(f)
        return data
    except (FileNotFoundError, json.JSONDecodeError):
        with open('cart.json', 'w') as f:
            json.dump([], f)
        return []


class Cart:
    def __init__(self, userId):
        self.userId = userId
        data = getDataCart()
        isFound = False
        for detail in data:
            if detail['userId'] == userId:
                self.savedMovies = detail['savedMovies']
                isFound = True
                break
        if not isFound:
            newUser = {
                "id": 1 if not data else data[-1]["id"] + 1,
                "userId": userId,
                "savedMovies": []
            }
            data.append(newUser)
            with open('cart.json', 'w') as f:
                json.dump(data, f, indent=4)

            self.savedMovies = []

    def saveMovie(self, movieId):
        data = getData()
        for movie in data:
            if movie['id'] == movieId:
                if movie['id'] in self.savedMovies:
                    self.savedMovies.remove(movie['id'])
                    data = getDataCart()
                    for details in data:
                        if details['userId'] == self.userId:
                            details['savedMovies'] = self.savedMovies
                            with open('cart.json', 'w') as f:
                                json.dump(data, f, indent=4)
                            break
                    return False
                else:
                    self.savedMovies.append(movie['id'])
                    data = getDataCart()
                    for details in data:
                        if details['userId'] == self.userId:
                            details['savedMovies'] = self.savedMovies
                            with open('cart.json', 'w') as f:
                                json.dump(data, f, indent=4)
                            break
                    return True
        return False

    def showSavedMovies(self):
        data = getData()
        movieIds = self.savedMovies
        for id in movieIds:
            for movie in data:
                if movie['id'] == id:
                    print("-" * len(movie['description']))
                    print(f"id: {movie['id']}")
                    print(f"Movie Name: {movie['name']}")
                    print(f"Movie description: {movie['description']}")
                    print(f"Movie Contry: {movie['country']}")
                    print(f"Movie Year: {movie['year']}")
                    print(f"Likes: {movie['likes']}")
                    print("-" * len(movie['description']))
