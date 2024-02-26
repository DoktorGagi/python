import random
import time
import os
print("Welcome to RockPaperScissors !!!")
print()
while True:
    tools = ["rock","paper","scissors"]
    player_choice = input("Chose: rock,paper or scissors?\n")
    pc_choice = random.choice(tools)
    print(pc_choice)
    if player_choice == pc_choice:
        print("No winner!")
    elif player_choice == "rock" and pc_choice == "scissors" or player_choice == "scissors" and pc_choice == "paper" or player_choice == "paper" and pc_choice == "rock":
        print("U win!!!")
    else:
        print("U loose!")
    time.sleep(3)
    os.system ("cls")