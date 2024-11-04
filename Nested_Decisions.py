# Task1: Code correction

place= input("Choose a place: forest or cave?")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else: 
        action == "cross a river"
        print("you found a boat!")
elif place == "cave":
    # Task2: Setting the scene
    light = input("light a torch or proceed in dark")
    if light == "light a torch":
        print("you find a hidden treasure!")
    else:
        light == "proceed in dark"
        print("You get lost")

# Task3: Default path

else:
    pass
