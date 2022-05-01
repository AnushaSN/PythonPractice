#Travis Security system,checks for user in list, if not prest asks if the user wants to be added,
#if present asks if the user wants to be removed
#known users list
known_users = ["Anu" , "Apoo" , "Shashu" , "Shilpa" , "Anna" , "Amma"]
#infinite loop
while True:
    print("Hello ! My name is Travis")
    name = input("What is your name ?:").strip().capitalize()

    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the system?(Y/N):").strip().upper()
        if remove == "Y":
            known_users.remove(name)
            print("Sorry to see you go :(") #adding message
            break #breaking out of loop once user is removed
        elif remove == "N":
            print("No problem! i did not want you to leave anyway!!")
    else:
        print("hmmm I don't think i have met you yet {}".format(name))
        add_me = input("Would you like to be added in the system?:(Y?N)").strip().upper()
        if add_me == 'Y':
            known_users.append(name)
            print("Added you to the list!") #adding confimation
        elif add_me == 'N':
            print("No worries, will see you around!")
