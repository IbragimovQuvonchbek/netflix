# first person who registers, is admin!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
from functions import signup, login, addMovie, showMovieList, likeMovie, showSavedMovies, saveMovie

print(
    '''                                                                   
                                           ""                       
                                                                    
88,dPYba,,adPYba,   ,adPPYba,  8b       d8 88  ,adPPYba, ,adPPYba,  
88P'   "88"    "8a a8"     "8a `8b     d8' 88 a8P_____88 I8[    ""  
88      88      88 8b       d8  `8b   d8'  88 8PP"""""""  `"Y8ba,   
88      88      88 "8a,   ,a8"   `8b,d8'   88 "8b,   ,aa aa    ]8I  
88      88      88  `"YbbdP"'      "8"     88  `"Ybbd8"' `"YbbdP"'  
    '''
)

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
            optionForAll = int(input("Back | Watch movies | Watch saved Movies| Add movie (0|1|2|3): "))
        else:
            optionForAll = int(input("Back | Watch movies | Watch saved Movies (0|1|2): "))

        if optionForAll == 0:
            break
        elif optionForAll == 1:
            showMovieList()
            while True:
                option2 = int(input("Back | Like movies | Save movie(0|1|2): "))
                if option2 == 0:
                    break
                elif option2 == 1:
                    movieId = int(input("Write movie id: "))
                    likeMovie(currentUser, movieId)
                elif option2 == 2:
                    movieId = int(input("Write movie id:     "))
                    saveMovie(currentUser, movieId)
        elif optionForAll == 2:
            showSavedMovies(currentUser)
        elif optionForAll == 3 and isAdmin:
            addMovie()
        else:
            print("invalid option")
