import os
import time
print()
print("Welcome to PythonPizza !!!")
print()

while True:
    pizza_size = input("What size of pizza would u like?\n").lower()
    pepperoni = input("Would you like pepperoni?\n").lower()
    extra_cheese = input("Would u like extra cheese on it?\n").lower()
    ammount = 0

    if pizza_size == "small":
        ammount = 15
        if pepperoni == "yes":
            ammount += 2
    elif pizza_size == "medium":
        ammount = 20
    elif pizza_size == "large":
        ammount = 25
    if pepperoni == "yes":
        ammount += 3
    if extra_cheese == "yes":
        ammount += 1
    print(f"That is {ammount} to pay for!")
    time.sleep(5)
    os.system("cls")