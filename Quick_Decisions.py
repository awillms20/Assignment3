# Task1: Code correction

attendees = int(input("Enter number of attendees"))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

#Task2: Venue selection

entertainment = "audio system" if attendees > 100 else "projector"
print(entertainment)

#Task3: Catering chocies

food = input("Do you want vegetarian, yes or no")
print("Veggie Delight Caterers") if food == "yes"  else print("Gourmet Meals Caterers")
