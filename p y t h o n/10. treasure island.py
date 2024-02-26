print("""Welcome to the TreasureIsland!!!""")
print()
print()
side = input("You came to crossroad so which side u wanna go now?\n")

if side == "left":
    print("You end up travelling to starvation so u died and its GAME OVER for you!\n")
elif side == "right":
    print("good choice my man,continue your travel to treasure!\n")
    water = input("Now its a dead water end do u wanna wait for boat or try to swim?\n")
if water == "swim":
    print("Oh no water was full of croc's and u died offcourse!\n")
    exit()
elif water == "boat":
    print("there was small boat coming with beatyfull girl paddling and she gave u ride of your life and offcourse u end up on shore...\n")
    castle = input(""""You found big castle and went inside and there is hallway with 
                       three dors.Now choose one to enter so what door will be your choice blue,red or yellow\n""")
if castle == "yellow":
    print("U win treasure and also boat girl,nicelly done,have fun!!!\n")
else:
    print("U dead bro GAME OVER for you,byee.")
