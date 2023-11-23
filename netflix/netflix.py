from functions import isAdmin, signup, login, addMovie, showMovieList, likeMovie


option = int(input("Sing up | Log in (0|1): "))
currentUser = 0
isAdmin = False
if option == 0:
    print("=========Sign up=============")
    register = signup()
    print("successfully registred" if register != 0 else "username already exists")
if option == 1 or option == 0:
    print("=========Log in==============")
    currentUser, isAdmin = login()
    print("success" if currentUser != 0 else "incorrect username or password")
elif option != 0 != 1:
    print("invalid option")
    
while True and currentUser != 0:
    optionForAll = 0
    if isAdmin:
        optionForAll = int(input("Exit | Watch movies |  Add movie (0|1|2): "))
    else:
        optionForAll = int(input("Exit | Watch movies (0|1): "))
        
    if optionForAll == 0:
        break     
    elif optionForAll == 1:
        showMovieList()
        while True:
            option2 = int(input("Exit | Like movies (0|1): "))
            if option2 == 0:
                break  
            elif option2 == 1:
                movieId = int(input("Write movie id: "))
                likeMovie(currentUser, movieId)
    elif optionForAll == 2 and isAdmin:
        addMovie()
    else:
        print("invalid option")
        
    
