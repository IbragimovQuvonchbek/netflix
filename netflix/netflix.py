# Admin-login:ibragimov10-password:abc123
from functions import signup, login, addMovie, showMovieList, likeMovie

while True:
    option = int(input("Exit | Sing up | Log in (0|1|2): "))
    currentUser = 0
    isAdmin = False
    if option == 1:
        print("=========Sign up=============")
        register = signup()
        print("successfully registred" if register != 0 else "username already exists")
    if option == 1 or option == 2:
        print("=========Log in==============")
        currentUser, isAdmin = login()
        print("success" if currentUser != 0 else "incorrect username or password")
    elif option == 0:
        break
    while True and currentUser != 0:
        optionForAll = 0
        if isAdmin:
            optionForAll = int(input("Back | Watch movies |  Add movie (0|1|2): "))
        else:
            optionForAll = int(input("Back | Watch movies (0|1): "))

        if optionForAll == 0:
            break
        elif optionForAll == 1:
            showMovieList()
            while True:
                option2 = int(input("Back | Like movies (0|1): "))
                if option2 == 0:
                    break
                elif option2 == 1:
                    movieId = int(input("Write movie id: "))
                    likeMovie(currentUser, movieId)
        elif optionForAll == 2 and isAdmin:
            addMovie()
        else:
            print("invalid option")
