#Model the program to tell which is the best trail

import random

#Define possible variables
temperature = None
weather = None
season = None
freshSnow = random.randint(0, 24)
timeOfDay = None





# Check if the time of day is within the valid range
while True:
    try:
        timeOfDay = int(input("Enter the time of day (8-16): "))
        if 8 <= timeOfDay <= 16 and timeOfDay % 1 == 0:
            break
        else:
            print("Invalid input. Please enter a time between 8am and 4pm in hourly increments.")
    except ValueError:
        print("Invalid input. Please enter a valid time.")


# Check if the season is within the valid options
while True:
    season = input("Enter the season (Winter/Spring): ")
    if season == "Winter" or season == "Spring":
        break
    else:
        print("Invalid input. Please enter either Winter or Spring.")


    


#Create trails which have a series of attributes