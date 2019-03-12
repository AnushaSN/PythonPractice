#program to check if the movie is currently running,if the age is appropriate and there are tickets available
# dictionary key:[age,seats left]
films ={"Finding Dory": [3,5],
        "Bourne":[18,5],
        "Tarzan":[15,5],
        "Ghost Busters":[12,5]
        }
while True:
    options=list(films.keys())
    print(options)
    choice = input("Which movie do you want to watch?:").strip().title()

    if choice in films:
        age = int(input("How old are you ?").strip())
        if age >= films[choice][0]:
            if films[choice][1]  > 0:
                print("enjoy the movie!")
                films[choice][1] = films[choice][1] - 1
            else:
                print("Sorry we are out of tickets !")
        else:
            print("You are too young to watch the movie")
        
    else:
        print("We don't have that film...")
