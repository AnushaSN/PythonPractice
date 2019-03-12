known_users = ["Anu" , "Apoo" , "Shashu" , "Shilpa" , "Anna" , "Amma"]

while True:
    print("Hello ! My name is Travis")
    name = input("What is your name ?:").strip().capitalize()

    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the system?(Y/N):").strip().upper()
        if remove == "Y":
            known_users.remove(name)
        elif remove == "N":
            print("No problem! i did not want you to leave anyway!!")
    else:
        print("hmmm I don't think i have met you yet {}".format(name))
        add_me = input("Would you like to be added in the system?:(Y?N)").strip().upper()
        if add_me == 'Y':
            known_users.append(name)
        elif add_me == 'N':
            print("No worries, will see you around!")
