import json
from hashlib import blake2b


def getData():
    try:
        with open('user.json') as f:
            data = json.load(f)
        return data
    except (FileNotFoundError, json.JSONDecodeError):
        with open('user.json', 'w') as f:
            json.dump([], f)
        return []


class User:
    id = 0

    def __init__(self, name, surname, username, password):
        self.name = name
        self.surname = surname
        self.username = username
        self.__password = password

    def createNewUser(self):
        if not self.isAvailable():
            data = getData()
            self.id = 1 if not data else data[-1]['id'] + 1
            newUser = {
                "id": self.id,
                "name": self.name,
                "surname": self.surname,
                "username": self.username,
                "password": blake2b(self.__password.encode('utf-8')).hexdigest(),
                "isAdmin": True if not data else False,
            }
            data.append(newUser)
            with open('user.json', 'w') as f:
                json.dump(data, f, indent=4)
            return True
        return False

    def isAvailable(self):
        data = getData()
        for user in data:
            if user['username'] == self.username:
                return True
        return False
