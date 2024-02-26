import time 
import os
while True:
    print("Welcome to RollerCoaster!!!")
    tickett = 0
    height = input("Are you higher than 120 cm?\n").lower()
    if height == "yes":
        print("You are allowed to go inside then")
        age = int(input("How old are you?\n"))
        if age >= 45 and age < 55:
            print("For you tickett is free!!! Enjoy!") 
        elif age >= 18:
            tickett = 12
            print("The price of ticket is",tickett,"euro's!")
        elif age <= 12:
            tickett = 5
            print("The price of ticket is",tickett,"euro's!")
        else:
            tickett = 7
            print("The price of tickett is",tickett,"euros!")
        pictures = input("Would you like pictures?\n")
        if pictures == "yes".lower():
            tickett += 3
            print("The price of ticket and pictures is: ",tickett)
    else:
        print("You are not alowed to go inside.Im sorry.")
    
    

    time.sleep(5)
    os.system("cls")