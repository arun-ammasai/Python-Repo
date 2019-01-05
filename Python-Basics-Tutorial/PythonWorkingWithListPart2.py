users =["Phil","Coulson","John","Dennis","Mic"]
print(users)

while True :
    print("Hello My name is Jarvis")
    name = input("What is your Name ? ").strip()

    if name in users :
        print("Welcome Mr.{}".format(name))

        remove = input("Would you like to removed from the system (y/n) ? :")
        if(remove == 'y') :
            users.remove(name)
        else :
            print("No Problem, I didn't want you to leave !")            
        print(users)
    else :
        print("I dont think you are exist in our system !")
        add = input("Would you like to added to the system (y/n) ? :")

        if(add == "y") :
            users.append(name)
            print(users)
        else :
            print("See You later !!!")
