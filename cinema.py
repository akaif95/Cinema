#THis program is designed to give a list of movies stored in a dictionary
#Then have the user pick one of the available films. It will also ask for
#The user's age and see if they are old enough to watch it


films = {
    "Finding Dory": [3,5],
    "Coraline": [12,7],
    "Shape of Water": [18,0],
    "Pan's Labryinth": [18,4],
    "Tarzan": [15,5], 

    }
print("Our available movies are as followed: ")
print()

for key in films:
    print(key)

print()

while True:
    
    choice = input("What movie would you like to watch?: ").strip().title()

    if choice in films:
        age = int(input("How old are you?: ").strip())

        if age >= films [choice][0]:

            num_seats = films[choice][1]

            if num_seats > 0:
                 print("Enjoy the film!")
                 films[choice][1] = films[choice][1] - 1
            else:
                print("Sorry, we are sold out!")
            
        else:
            print("You are too young to see the film.")
           
    else:
        print("I'm sorry, that movie is not playing in this theatre.")
    
